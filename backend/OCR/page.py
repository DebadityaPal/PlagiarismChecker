import cv2
import numpy as np
from OCR.utils import resize


def fourCornersSort(pts):
    """Sort corners: top-left, bot-left, bot-right, top-right"""
    # Difference and sum of x and y value
    diff = np.diff(pts, axis=1)
    summ = pts.sum(axis=1)

    # Top-left point has smallest sum...
    # np.argmin() returns INDEX of min
    return np.array(
        [
            pts[np.argmin(summ)],
            pts[np.argmax(diff)],
            pts[np.argmax(summ)],
            pts[np.argmin(diff)],
        ]
    )


def contourOffset(cnt, offset):
    """Offset contour, by 5px border"""
    # Matrix addition
    cnt += offset

    # if value < 0 => replace it by 0
    cnt[cnt < 0] = 0
    return cnt


def pageDetection(image):

    img = cv2.cvtColor(resize(image), cv2.COLOR_BGR2GRAY)
    img = cv2.bilateralFilter(img, 9, 75, 75)
    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 4
    )
    img = cv2.medianBlur(img, 11)
    img = cv2.copyMakeBorder(img, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    edges = cv2.Canny(img, 200, 250)
    # Getting contours
    contours, hierarchy = cv2.findContours(
        edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    # Finding contour of biggest rectangle
    # Otherwise return corners of original image
    height = edges.shape[0]
    width = edges.shape[1]
    MAX_COUNTOUR_AREA = (width - 10) * (height - 10)

    # Page fill at least half of image, then saving max area found
    maxAreaFound = MAX_COUNTOUR_AREA * 0.5

    # Saving page contour
    pageContour = np.array(
        [[5, 5], [5, height - 5], [width - 5, height - 5], [width - 5, 5]]
    )

    # Go through all contours
    for cnt in contours:
        # Simplify contour
        perimeter = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.03 * perimeter, True)

        # Page has 4 corners and it is convex
        # Page area must be bigger than maxAreaFound
        if (
            len(approx) == 4
            and cv2.isContourConvex(approx)
            and maxAreaFound < cv2.contourArea(approx) < MAX_COUNTOUR_AREA
        ):

            maxAreaFound = cv2.contourArea(approx)
            pageContour = approx

    # Sort and offset corners
    pageContour = fourCornersSort(pageContour[:, 0])
    pageContour = contourOffset(pageContour, (-5, -5))

    # Recalculate to original scale - start Points
    sPoints = pageContour.dot(image.shape[0] / 800)

    # Using Euclidean distance
    # Calculate maximum height (maximal length of vertical edges) and width
    height = max(
        np.linalg.norm(sPoints[0] - sPoints[1]), np.linalg.norm(sPoints[2] - sPoints[3])
    )
    width = max(
        np.linalg.norm(sPoints[1] - sPoints[2]), np.linalg.norm(sPoints[3] - sPoints[0])
    )

    # Create target points
    tPoints = np.array([[0, 0], [0, height], [width, height], [width, 0]], np.float32)

    # getPerspectiveTransform() needs float32
    if sPoints.dtype != np.float32:
        sPoints = sPoints.astype(np.float32)

    # Wraping perspective
    M = cv2.getPerspectiveTransform(sPoints, tPoints)
    newImage = cv2.warpPerspective(image, M, (int(width), int(height)))

    return newImage

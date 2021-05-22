import cv2
import numpy as np
from utils import resize, ratio


def bb_to_img(img, lines):
    result = []
    for line in lines:
        for word in line:
            result.append(img[word[1] : word[3], word[0] : word[2]])
    return result


def wordDetection(image, join=False):
    """Detecting the words bounding boxes.
    Return: numpy array of bounding boxes [x, y, x+w, y+h]
    """
    # Preprocess image for word detection
    blurred = cv2.GaussianBlur(image, (5, 5), 18)
    edge_img = edgeDetection(blurred)
    ret, edge_img = cv2.threshold(edge_img, 50, 255, cv2.THRESH_BINARY)
    preprocessed_image = cv2.morphologyEx(
        edge_img, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8)
    )

    return textDetection(preprocessed_image, image, join)


def sort_words(boxes):
    """Sort boxes - (x, y, x+w, y+h) from left to right, top to bottom."""
    mean_height = sum([y2 - y1 for _, y1, _, y2 in boxes]) / len(boxes)

    boxes.view("i8,i8,i8,i8").sort(order=["f1"], axis=0)
    current_line = boxes[0][1]
    lines = []
    tmp_line = []
    for box in boxes:
        if box[1] > current_line + mean_height:
            lines.append(tmp_line)
            tmp_line = [box]
            current_line = box[1]
            continue
        tmp_line.append(box)
    lines.append(tmp_line)

    for line in lines:
        line.sort(key=lambda box: box[0])

    return lines


def edgeDetection(im):
    """
    Edge detection using sobel operator on each layer individually.
    Sobel operator is applied for each image layer (RGB)
    """
    return np.max(
        np.array(
            [
                sobelFilter(im[:, :, 0]),
                sobelFilter(im[:, :, 1]),
                sobelFilter(im[:, :, 2]),
            ]
        ),
        axis=0,
    )


def sobelFilter(channel):
    """Sobel operator."""
    sobelX = cv2.Sobel(channel, cv2.CV_16S, 1, 0)
    sobelY = cv2.Sobel(channel, cv2.CV_16S, 0, 1)
    sobel = np.hypot(sobelX, sobelY)
    sobel[sobel > 255] = 255
    return np.uint8(sobel)


def textDetection(img, image, join=False):
    """Text detection using contours."""
    small = resize(img, 2000)

    # Finding contours
    mask = np.zeros(small.shape, np.uint8)
    cnt, hierarchy = cv2.findContours(
        np.copy(small), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
    )

    index = 0
    boxes = []
    if cnt:
        # Go through all contours in top level
        while index >= 0:
            x, y, w, h = cv2.boundingRect(cnt[index])
            cv2.drawContours(mask, cnt, index, (255, 255, 255), cv2.FILLED)
            maskROI = mask[y : y + h, x : x + w]
            # Ratio of white pixels to area of bounding rectangle
            r = cv2.countNonZero(maskROI) / (w * h)

            # Limits for text
            if (
                r > 0.1
                and 1600 > w > 10
                and 1600 > h > 10
                and h / w < 3
                and w / h < 10
                and (60 // h) * w < 1000
            ):
                boxes += [[x, y, w, h]]

            index = hierarchy[0][index][0]

        # image for drawing bounding boxes
        small = cv2.cvtColor(small, cv2.COLOR_GRAY2RGB)
        bounding_boxes = np.array([0, 0, 0, 0])
        for (x, y, w, h) in boxes:
            cv2.rectangle(small, (x, y), (x + w, y + h), (0, 255, 0), 2)
            bounding_boxes = np.vstack((bounding_boxes, np.array([x, y, x + w, y + h])))
        cv2.imwrite("./boxes.jpg", cv2.cvtColor(small, cv2.COLOR_BGR2RGB))

        boxes = bounding_boxes.dot(ratio(image, small.shape[0])).astype(np.int64)
        return boxes[1:]
    else:
        return boxes

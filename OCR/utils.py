import cv2


def resize(img, height=800):
    """Resize image to given height"""
    ratio = height / img.shape[0]
    return cv2.resize(img, (int(ratio * img.shape[1]), height))


def ratio(img, height=800):
    """Getting scale ratio."""
    return img.shape[0] / height

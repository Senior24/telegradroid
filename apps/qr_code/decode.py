import cv2
import numpy as np

from typing import List


def decode_qr(img: np.ndarray) -> List[str]:
    detector = cv2.QRCodeDetector()

    retval, decoded_info, points, _ = detector.detectAndDecodeMulti(img)

    if retval and decoded_info:
        return [data for data in decoded_info if data]

    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        return [data]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.equalizeHist(gray)

    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31, 2
    )

    retval, decoded_info, points, _ = detector.detectAndDecodeMulti(thresh)

    if retval and decoded_info:
        return [data for data in decoded_info if data]

    return []

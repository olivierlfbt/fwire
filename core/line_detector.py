import cv2

from config import (
    HOUGH_THRESHOLD,
    MIN_LINE_LENGTH,
    MAX_LINE_GAP
)


class LineDetector:

    def detect(self, frame):

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        edges = cv2.Canny(
            gray,
            60,
            150
        )

        lines = cv2.HoughLinesP(
            edges,
            1,
            3.14159 / 180,
            threshold=HOUGH_THRESHOLD,
            minLineLength=MIN_LINE_LENGTH,
            maxLineGap=MAX_LINE_GAP
        )

        if lines is None:
            return []

        return [line[0] for line in lines]

import cv2

from config import VIDEO_FILE


class FrameLoader:

    def __init__(self):
        self.capture = cv2.VideoCapture(
            str(VIDEO_FILE)
        )

    def frames(self):

        while self.capture.isOpened():

            success, frame = self.capture.read()

            if not success:
                break

            yield frame

        self.capture.release()

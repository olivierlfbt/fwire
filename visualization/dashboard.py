import cv2

from config import WINDOW_NAME


class Dashboard:

    def show(self, frame):

        cv2.imshow(
            WINDOW_NAME,
            frame
        )

        cv2.waitKey(1)

    def close(self):

        cv2.destroyAllWindows()

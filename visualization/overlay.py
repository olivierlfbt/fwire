import cv2


class Overlay:

    def draw(self, frame, wires):

        for wire in wires:

            cv2.line(

                frame,

                (wire["x1"], wire["y1"]),

                (wire["x2"], wire["y2"]),

                (0, 255, 0),

                2

            )

        return frame

import math


class Geometry:

    @staticmethod
    def line_length(wire):

        dx = wire["x2"] - wire["x1"]

        dy = wire["y2"] - wire["y1"]

        return math.sqrt(
            dx * dx +
            dy * dy
        )

    @staticmethod
    def midpoint(wire):

        return (

            (wire["x1"] + wire["x2"]) / 2,

            (wire["y1"] + wire["y2"]) / 2

        )

from config import WARNING_DISTANCE


class ProximityAlert:

    def check(self, wires):

        warning = False

        for wire in wires:

            distance = abs(
                wire["x2"] - wire["x1"]
            )

            if distance < WARNING_DISTANCE:

                warning = True

                print(
                    "[WARNING] Power line is nearby."
                )

        return warning

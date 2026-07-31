class WireTracker:

    def __init__(self):
        self.previous = []

    def update(self, lines):

        tracked = []

        for line in lines:

            tracked.append({
                "x1": int(line[0]),
                "y1": int(line[1]),
                "x2": int(line[2]),
                "y2": int(line[3])
            })

        self.previous = tracked

        return tracked

    def last(self):

        return self.previous

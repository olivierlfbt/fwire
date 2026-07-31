from core.frame_loader import FrameLoader
from core.line_detector import LineDetector
from core.wire_tracker import WireTracker
from core.proximity_alert import ProximityAlert


def main():

    loader = FrameLoader()
    detector = LineDetector()
    tracker = WireTracker()
    alert = ProximityAlert()

    for frame in loader.frames():

        lines = detector.detect(frame)

        tracked = tracker.update(lines)

        alert.check(tracked)

        print(
            f"Detected {len(tracked)} power lines"
        )


if __name__ == "__main__":
    main()

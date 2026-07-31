from pathlib import Path

BASE_DIR = Path(__file__).parent

VIDEO_FILE = BASE_DIR / "data" / "sample.mp4"

CALIBRATION_FILE = (
    BASE_DIR / "data" / "calibration.json"
)

OUTPUT_DIR = BASE_DIR / "output"

HOUGH_THRESHOLD = 90

MIN_LINE_LENGTH = 80

MAX_LINE_GAP = 15

WARNING_DISTANCE = 60

WINDOW_NAME = "Power Line Inspector"

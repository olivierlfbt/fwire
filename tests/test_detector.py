import unittest
import numpy as np

from core.line_detector import LineDetector


class LineDetectorTest(unittest.TestCase):

    def setUp(self):
        self.detector = LineDetector()

    def test_detect_returns_list(self):

        frame = np.zeros(
            (480, 640, 3),
            dtype=np.uint8
        )

        lines = self.detector.detect(frame)

        self.assertIsInstance(
            lines,
            list
        )

    def test_empty_frame(self):

        frame = np.zeros(
            (240, 320, 3),
            dtype=np.uint8
        )

        result = self.detector.detect(frame)

        self.assertEqual(
            result,
            []
        )


if __name__ == "__main__":
    unittest.main()

import json
from pathlib import Path
from datetime import datetime


class ReportGenerator:

    def __init__(self):
        self.output = Path("output")

        self.output.mkdir(
            exist_ok=True
        )

    def save(self, processed_frames, detected_lines):

        report = {

            "created": datetime.now().isoformat(),

            "processedFrames": processed_frames,

            "detectedPowerLines": detected_lines

        }

        file = self.output / "inspection_report.json"

        with open(file, "w") as fp:

            json.dump(
                report,
                fp,
                indent=4
            )

        return file

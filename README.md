# Power Line Inspector

Power Line Inspector is a computer vision application that detects power transmission lines in drone video streams.

The system uses Hough Transform to identify wires, tracks detected lines between frames, and warns the operator when the drone approaches a power line.

## Features

- Video processing
- Hough Line Transform
- Wire detection
- Wire tracking
- Distance estimation
- Proximity warning
- Overlay visualization
- Processing report

## Project Structure

```
core/
visualization/
utils/
data/
tests/
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## License

MIT

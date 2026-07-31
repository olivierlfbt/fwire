# Architecture

```
             app.py
                │
                ▼
         FrameLoader
                │
                ▼
         LineDetector
                │
                ▼
          WireTracker
                │
        ┌───────┴────────┐
        ▼                ▼
 ProximityAlert     Overlay
        │                │
        └───────┬────────┘
                ▼
           Dashboard
                │
                ▼
        ReportGenerator
```

## Modules

### FrameLoader

Reads frames from the drone video.

### LineDetector

Detects transmission lines using the Probabilistic Hough Transform.

### WireTracker

Tracks detected wires between consecutive frames.

### ProximityAlert

Estimates whether detected wires are too close to the drone.

### Overlay

Draws detected power lines on each processed frame.

### Dashboard

Displays the processed video stream.

### ReportGenerator

Generates a JSON inspection report after processing.

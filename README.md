# Wanda-Vision Magic Hand Effect

This project uses AI-powered hand tracking to create a real-time Wanda-style magic effect on your webcam feed. Built with Python, OpenCV, and MediaPipe, it's a beginner-friendly introduction to computer vision and interactive effects.

## Features

- Real-time hand detection using MediaPipe
- Magic glow effect drawn on your hand (like Wanda Maximoff in the MCU)
- Easy to run and extend

## Requirements

- Python 3.10 or 3.11 (MediaPipe does **not** support Python 3.12+)
- Webcam

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/sarrazer24/wanda-vision.git
   cd wanda-vision
   ```

2. **Create and activate a virtual environment (recommended):**

   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Make sure your webcam is connected.
2. Run the main script:
   ```sh
   python src/main.py
   ```
3. Move your hand in front of the camera and watch the magic effect appear!

## Project Structure

```
wanda-vision/
  README.md
  requirements.txt
  src/
    main.py
    effects/
      magic.py
    models/
      hand_tracking.py
    utils/
      helpers.py
```

- `main.py`: Runs the application.
- `effects/magic.py`: Draws the magic effect.
- `models/hand_tracking.py`: Handles hand detection.
- `utils/helpers.py`: (Optional) Helper functions.

## Troubleshooting

- If you get an error about `mediapipe` not installing, make sure you are using Python 3.10 or 3.11.
- If your webcam doesn't turn on, check that it's not being used by another application.

## Credits

- [MediaPipe](https://google.github.io/mediapipe/) for hand tracking
- [OpenCV](https://opencv.org/) for video processing

---

Enjoy your Wanda-Vision

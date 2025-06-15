# wanda-vision

## Overview
Wanda Vision is a project that utilizes computer vision to detect hand movements and display magical effects on the screen, inspired by the magic effects seen in the MCU.

## Project Structure
```
wanda-vision
├── src
│   ├── main.py          # Entry point of the application
│   ├── effects
│   │   └── magic.py     # Contains the MagicEffect class for rendering effects
│   ├── models
│   │   └── hand_tracking.py # Contains the HandTracker class for hand detection
│   └── utils
│       └── helpers.py    # Utility functions for model loading and frame preprocessing
├── requirements.txt      # Lists project dependencies
├── README.md             # Project documentation
└── .gitignore            # Files to ignore in version control
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/wanda-vision.git
   cd wanda-vision
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```
Ensure that your camera is accessible and that the necessary permissions are granted.

## Functionality
- The application captures video input from the camera.
- It processes hand movements using a computer vision model.
- Based on the detected movements, magical effects are rendered on the screen.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
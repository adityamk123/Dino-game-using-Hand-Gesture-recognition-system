## Dino game using Hand Gesture recognition system

 Dino Game Controlled by Hand Gestures
This project allows you to play the Google Chrome Dino Game using your hand gestures instead of the keyboard.
By leveraging Python, OpenCV, and MediaPipe, the system detects your hand movements from the webcam and sends keyboard inputs to control the dinosaur.

## FEATURES: 
 ```
 -Real-time hand tracking using your webcam
 -Gesture-based control
 -Open palm → Jump
 (You can customize gestures for duck, pause, etc.)
 -Play the Dino Game without touching your keyboard
 -Works smoothly in VS Code with Python virtual environment
```

 ## TECH STACK & LIBRARIES:
```
-Python 3.8+
-OpenCV (cv2) → For webcam video capture
-MediaPipe → For hand gesture recognition
-PyAutoGUI → For simulating keyboard presses (space key for jump)
-Keyboard (optional) → For alternative control of key inputs
-PyWin32 (win32gui, win32con) → To ensure Chrome Dino window stays active
```

 ## PROJECT STRUCTRES:
``` bash
dino_game_handgesture/
│── hand_gesture_control.py   # Main Python script
│── venv/                     # Virtual environment (not uploaded to GitHub)
│── README.md                 # Project documentation
```

## INSTALLATION & SETUP:
```bash
 -Clone the Repository
git clone https://github.com/your-username/dino-game-handgesture.git
cd dino-game-handgesture
 -Create Virtual Environment
python -m venv venv
 -Activate it:
Windows (PowerShell):
.\venv\Scripts\activate
Linux/MacOS:
source venv/bin/activate
 -Install Dependencies
pip install opencv-python mediapipe pyautogui pywin32
(If needed, also install keyboard.)
```

## How to Run:
```
-Open VS Code inside the project folder
-Run the script
-python hand_gesture_control.py
-Make sure your webcam is connected
-Open the Dino Game in Chrome:
-chrome://dino
(or open Chrome, turn off WiFi, and press spacebar)
-Show your hand gesture → Dino jumps!
```
## Troubleshooting
```
Dino not jumping after restart → Click on the Chrome window to refocus it
Webcam freezing → Reduce resolution in cv2.VideoCapture(0)
ModuleNotFoundError → Make sure all required libraries are installed inside your venv
```

## Future Improvements

Add gesture for ducking (fist gesture)
Add score tracking overlay
Improve gesture recognition accuracy
Deploy as an exe file for easy use

## Authors

Aditya M Khiroji  Email: adityakhiroji7@gmail.com
Chinmayi C  Email: chinnnn2202@gmail.com

Enjoy playing the Dino game with your hands! 🦖

# Project1
Eye Controlled Mouse Application
Overview
The Eye Controlled Mouse Application is a Python program that allows users to control their computer's cursor and perform clicks using their eyes. This application leverages OpenCV for video capture, MediaPipe for face mesh detection, and PyAutoGUI for cursor control and clicking.
It includes the following key features:
Camera Integration: Captures live video and processes it for facial landmark detection.
Face Mesh Processing: Detects facial features and tracks eye landmarks using MediaPipe.
Cursor Movement: Moves the cursor based on eye movements.
Blink Detection: Detects eye blinks to perform mouse clicks.

Prerequisites
Before running the program, ensure the following dependencies are installed:
Python 3.7+
OpenCV: Install with pip install opencv-contrib-python.
MediaPipe: Install with pip install mediapipe.
PyAutoGUI: Install with pip install pyautogui.
Additionally, ensure that your webcam is properly configured and functional.

Modules
1. CameraHandler Class
Handles all webcam operations, including:
Opening the camera.
Capturing individual frames.
Releasing the camera and closing OpenCV windows.
Public Methods:
open_camera(): Opens the video capture device. Raises an error if the webcam is inaccessible.
read_frame(): Reads a single frame from the webcam. Ensures the camera is initialized before reading.
release_camera(): Releases webcam resources and closes OpenCV windows.

2. FaceMeshHandler Class
Processes the video feed using MediaPipe’s FaceMesh to detect facial landmarks.
Public Methods:
__init__():
Initializes the MediaPipe FaceMesh model with refined landmarks.
process_frame(frame):
Converts the frame to RGB format.
Returns MediaPipe's facial landmark detection results.

3. EyeMouseController Class
Controls mouse actions based on detected facial landmarks and screen dimensions.
Public Methods:
__init__():
Fetches screen dimensions using pyautogui.size().
move_cursor(landmark):
Moves the cursor to specific screen coordinates derived from detected eye landmarks.
detect_blink(landmarks, frame_w, frame_h, frame):
Detects blinking by comparing eye landmark positions.
Performs a mouse click when a blink is detected.

4. EyeControlledMouseApp Class
Combines the CameraHandler, FaceMeshHandler, and EyeMouseController to create the interactive experience.
Public Methods:
__init__():
Initializes all components required for the application.
run():
Executes the main program loop:
Opens the webcam using CameraHandler.
Captures and processes frames.
Tracks eye landmarks for cursor movement and click detection.
Displays real-time video feed with annotations.
Releases system resources after exiting.

Core Workflow
Initialize Camera:


The CameraHandler opens the webcam and captures video frames in real time.
Process Frames with FaceMesh:


The FaceMeshHandler processes each frame to extract facial landmarks.
Eye landmarks are identified to control mouse actions.
Control Cursor and Detect Blinks:


Coordinates of specific eye landmarks are scaled to the screen size to move the cursor.
Blinks are detected by comparing specific y-coordinates of eye landmarks to trigger clicks.
Display Video:


The processed video feed is displayed using OpenCV, annotated with eye landmarks and movement tracking.
Clean Up:


The camera and any OpenCV resources are released when the application exits.

How to Run the Application
Install Dependencies: Ensure the required Python libraries are installed by running:
pip install opencv-python mediapipe pyautogui
Run the Script: Execute the program in your terminal:
python <script_name>.py
Replace <script_name> with the name of your Python script.
Usage:
Ensure your face is visible to the webcam.
Move your eyes to control the cursor.
Close your eye (blink) to perform a click.
Press 'q' to exit the application.

Key Features
Cursor Movement:


The cursor is moved in real-time based on the position of the user's eyes.
Blink Click Detection:


A blink is detected using the y-coordinates of specific eye landmarks. The application clicks the mouse when a blink is detected.
Mirror-Effect Video Feed:


The displayed video feed is flipped horizontally to create a mirrored view for more intuitive interaction.
Screen Compatibility:


The cursor movement scales automatically according to the user’s screen resolution.

Error Handling
Webcam Access:
If the webcam cannot be accessed, a RuntimeError is raised with an appropriate message.
Frame Read Error:
If frames cannot be captured from the webcam, a runtime exception is raised.
Graceful Exit:
All resources are released when the user exits or an error occurs.

Limitations
Requires proper lighting for accurate facial landmark detection.
Cursor movement may not be perfectly smooth on low-spec hardware.
Works best with a single user and a well-positioned webcam.

Future Improvements
Add support for multiple webcams.
Smoothen cursor motion using interpolation techniques.
Enhance blink detection accuracy with machine learning.

Acknowledgments
This project uses the following libraries:
OpenCV: For video capture and frame manipulation.
MediaPipe: For facial landmark and eye tracking.
PyAutoGUI: For screen control and mouse simulation.



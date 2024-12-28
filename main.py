import cv2
import mediapipe as mp
import pyautogui

# Class to handle camera operations
class CameraHandler:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cam = None

    # Open the camera
    def open_camera(self):
        self.cam = cv2.VideoCapture(self.camera_index)
        if not self.cam.isOpened():
            raise RuntimeError("Error: Could not access the webcam.")

    # Read a single frame from the camera
    def read_frame(self):
        if self.cam is None or not self.cam.isOpened():
            raise RuntimeError("Error: Camera is not initialized.")
        ret, frame = self.cam.read()
        if not ret:
            raise RuntimeError("Error: Failed to read from the webcam.")
        return frame

    # Release the camera and close any OpenCV windows
    def release_camera(self):
        if self.cam:
            self.cam.release()
            cv2.destroyAllWindows()

# Class to handle face mesh processing using MediaPipe
class FaceMeshHandler:
    def __init__(self):
        # Initialize FaceMesh with refined landmarks
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

    # Process a video frame and return the facial landmarks
    def process_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.face_mesh.process(rgb_frame)

# Class to control mouse actions based on facial landmarks
class EyeMouseController:
    def __init__(self):
        # Get screen dimensions
        self.screen_w, self.screen_h = pyautogui.size()

    # Move the cursor to a specific position based on landmark coordinates
    def move_cursor(self, landmark):
        screen_x = int(landmark.x * self.screen_w)
        screen_y = int(landmark.y * self.screen_h)
        pyautogui.moveTo(screen_x, screen_y)

    # Detect eye blink and perform a mouse click
    @staticmethod
    def detect_blink(landmarks, frame_w, frame_h, frame):
        # Coordinates for the left eye
        left_eye = [landmarks[145], landmarks[159]]
        for landmark in left_eye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))  # Draw circles on the eye landmarks
        # Check for blink by comparing y-coordinates
        if abs(left_eye[0].y - left_eye[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

# Main application class to combine all components
class EyeControlledMouseApp:
    def __init__(self):
        self.camera_handler = CameraHandler()  # Handles camera operations
        self.face_mesh_handler = FaceMeshHandler()  # Handles face mesh processing
        self.eye_mouse_controller = EyeMouseController()  # Controls mouse based on eye movements

    # Run the application
    def run(self):
        try:
            self.camera_handler.open_camera()  # Open the camera
            while True:
                frame = self.camera_handler.read_frame()  # Read a frame from the camera
                frame = cv2.flip(frame, 1)  # Flip the frame horizontally for a mirror effect
                output = self.face_mesh_handler.process_frame(frame)  # Process the frame to get landmarks
                frame_h, frame_w, _ = frame.shape

                # Check if facial landmarks are detected
                if output.multi_face_landmarks:
                    landmarks = output.multi_face_landmarks[0].landmark

                    # Highlight eye landmarks
                    for landmark_id, landmark in enumerate(landmarks[474:478]):
                        x = int(landmark.x * frame_w)
                        y = int(landmark.y * frame_h)
                        cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)  # Draw circles on landmarks
                        if landmark_id == 1:
                            self.eye_mouse_controller.move_cursor(landmark)  # Move cursor

                    # Detect blink and perform a click if detected
                    EyeMouseController.detect_blink(landmarks, frame_w, frame_h, frame)

                # Display the video feed
                cv2.imshow('Eye Controlled Mouse', frame)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except Exception as e:
            print("Error: " + str(e))  # Print any errors that occur
        finally:
            self.camera_handler.release_camera()  # Release the camera and close windows

# Entry point for the application
if __name__ == "__main__":
    app = EyeControlledMouseApp()  # Create an instance of the app
    app.run()  # Run the app

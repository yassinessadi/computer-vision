import cv2
import mediapipe as mp
import time

class HandDetector:
    def __init__(self, max_number_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=max_number_hands, 
                                         min_detection_confidence=detection_confidence, 
                                         min_tracking_confidence=tracking_confidence)
        self.mp_drawing = mp.solutions.drawing_utils
        self.previous_time = 0

    def detect_hands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
        return results

    def find_position(self, img, results, hand_num=0):
        """
        Find position for a single hand specified by hand_num (default is 0 for the first hand).
        """
        landmark_positions = []
        if results.multi_hand_landmarks and len(results.multi_hand_landmarks) > hand_num:
            handLms = results.multi_hand_landmarks[hand_num]
            for id, land_marks in enumerate(handLms.landmark):
                height, width, channel = img.shape
                position_x, position_y = int(land_marks.x * width), int(land_marks.y * height)
                landmark_positions.append((id, position_x, position_y))
            self.mp_drawing.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)
        return landmark_positions

    def display_fps(self, img):
        current_time = time.time()
        fps = 1 / (current_time - self.previous_time)
        self.previous_time = current_time
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    def release_resources(self):
        self.cap.release()
        cv2.destroyAllWindows()

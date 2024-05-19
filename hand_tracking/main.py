from hand_Detector import HandDetector
import cv2

def main():
    detector = HandDetector()
    while True:
        success, img = detector.cap.read()
        if not success:
            break

        results = detector.detect_hands(img)
        res = detector.find_position(img, results, hand_num=0) 
        if len(res) != 0:
            print(res[3])

        detector.display_fps(img)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    detector.release_resources()

if __name__ == "__main__":
    main()































# import cv2
# import mediapipe as mp
# import time

# class HandDetector:
#     def __init__(self, max_number_hands=2, detection_confidence=0.5, tracking_confidence=0.5):
#         self.cap = cv2.VideoCapture(0)
#         self.mp_hands = mp.solutions.hands
#         self.hands = self.mp_hands.Hands(max_num_hands=max_number_hands, 
#                                          min_detection_confidence=detection_confidence, 
#                                          min_tracking_confidence=tracking_confidence)
#         self.mp_drawing = mp.solutions.drawing_utils
#         self.previous_time = 0

#     def detect_hands(self):
#         while True:
#             success, img = self.cap.read()
#             if not success:
#                 break

#             imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#             results = self.hands.process(imgRGB)

#             res = self.find_position(img, results)
#             if len(res) != 0:
#                 print(res[3])

#             self._display_fps(img)
#             cv2.imshow("Image", img)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#         self.cap.release()
#         cv2.destroyAllWindows()

#     def find_position(self, img, results):
#         landmark_positions = []
#         if results.multi_hand_landmarks:
#             for handLms in results.multi_hand_landmarks:
#                 for id, land_marks in enumerate(handLms.landmark):
#                     height, width, channel = img.shape
#                     position_x, position_y = int(land_marks.x * width), int(land_marks.y * height)
#                     landmark_positions.append((id, position_x, position_y))
#                     # if id == 4:
#                     #     cv2.circle(img, (position_x, position_y), 15, (25, 10, 255), cv2.FILLED)
#                 self.mp_drawing.draw_landmarks(img, handLms, self.mp_hands.HAND_CONNECTIONS)
#         return landmark_positions

#     def _display_fps(self, img):
#         current_time = time.time()
#         fps = 1 / (current_time - self.previous_time)
#         self.previous_time = current_time
#         cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

# if __name__ == "__main__":
#     detector = HandDetector()
#     detector.detect_hands()

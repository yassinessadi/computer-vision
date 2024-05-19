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
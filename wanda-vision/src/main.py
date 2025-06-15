import cv2
from models.hand_tracking import HandTracker
from effects.magic import draw_magic_effect

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        results = tracker.find_hands(frame)
        hand_landmarks = results.multi_hand_landmarks if results.multi_hand_landmarks else []
        draw_magic_effect(frame, hand_landmarks)
        tracker.draw_hands(frame, hand_landmarks)
        cv2.imshow("Wanda-Vision Magic", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
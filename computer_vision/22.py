import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

FINGER_NAMES = ["Thumb", "Index", "Middle", "Ring", "Pinky"]

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

for i in range(30):
    cap.read()

with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                # Main droite ou gauche
                hand_label = results.multi_handedness[i].classification[0].label
                if hand_label == "Right":
                    hand_label = "Right Hand"
                else:
                    hand_label = "Left Hand"

                # Dessiner les points
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Points du bout de chaque doigt
                finger_tips = [4, 8, 12, 16, 20]
                h, w, _ = frame.shape

                for j, tip_id in enumerate(finger_tips):
                    lm = hand_landmarks.landmark[tip_id]
                    x, y = int(lm.x * w), int(lm.y * h)
                    cv2.putText(frame, FINGER_NAMES[j], (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Afficher droite/gauche en haut
                wrist = hand_landmarks.landmark[0]
                wx, wy = int(wrist.x * w), int(wrist.y * h)
                cv2.putText(frame, hand_label, (wx - 30, wy - 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        cv2.imshow('Hand Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
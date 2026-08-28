import cv2
import mediapipe as mp
import random

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Historique des positions de chaque doigt
historique = {i: [] for i in range(5)}
couleurs = [
    (255, 0, 0),    # Thumb - bleu
    (0, 255, 0),    # Index - vert
    (0, 0, 255),    # Middle - rouge
    (255, 255, 0),  # Ring - jaune
    (0, 255, 255),  # Pinky - cyan
]

finger_tips = [4, 8, 12, 16, 20]
MAX_POINTS = 30  # longueur de la traînée

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
for i in range(30):
    cap.read()

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # miroir
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                h, w, _ = frame.shape

                for j, tip_id in enumerate(finger_tips):
                    lm = hand_landmarks.landmark[tip_id]
                    x, y = int(lm.x * w), int(lm.y * h)

                    # Ajouter la position à l'historique
                    historique[j].append((x, y))
                    if len(historique[j]) > MAX_POINTS:
                        historique[j].pop(0)

                    # Dessiner la traînée
                    for k in range(1, len(historique[j])):
                        epaisseur = int(k * 5 / MAX_POINTS) + 1
                        cv2.line(frame, historique[j][k-1], historique[j][k],
                                 couleurs[j], epaisseur)

                    # Point brillant au bout du doigt
                    cv2.circle(frame, (x, y), 8, couleurs[j], -1)

        cv2.imshow('Finger Paint', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
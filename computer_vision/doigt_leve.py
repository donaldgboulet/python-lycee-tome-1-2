import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
for i in range(30):
    cap.read()

# Canevas de dessin
canvas = np.zeros((480, 640, 3), dtype=np.uint8)

couleurs = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (0, 255, 255), (255, 0, 255)]
couleur_index = 0
prev_x, prev_y = 0, 0

def doigt_leve(landmarks, doigt_tip, doigt_pip):
    return landmarks[doigt_tip].y < landmarks[doigt_pip].y

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                lm = hand_landmarks.landmark

                # Détecter quels doigts sont levés
                index_leve  = doigt_leve(lm, 8, 6)
                majeur_leve = doigt_leve(lm, 12, 10)
                annul_leve  = doigt_leve(lm, 16, 14)
                auricu_leve = doigt_leve(lm, 20, 18)
                pouce_leve  = lm[4].x < lm[3].x  # pour main droite

                # Position de l'index
                ix = int(lm[8].x * w)
                iy = int(lm[8].y * h)

                # POING = effacer
                if not index_leve and not majeur_leve and not annul_leve:
                    canvas = np.zeros((480, 640, 3), dtype=np.uint8)
                    cv2.putText(frame, "EFFACE", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    prev_x, prev_y = 0, 0

                # POUCE + INDEX = changer couleur
                elif pouce_leve and index_leve and not majeur_leve:
                    couleur_index = (couleur_index + 1) % len(couleurs)
                    cv2.putText(frame, "COULEUR", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                    prev_x, prev_y = 0, 0

                # INDEX SEUL = dessiner
                elif index_leve and not majeur_leve:
                    if prev_x != 0 and prev_y != 0:
                        cv2.line(canvas, (prev_x, prev_y), (ix, iy),
                                 couleurs[couleur_index], 5)
                    prev_x, prev_y = ix, iy
                    cv2.circle(frame, (ix, iy), 8, couleurs[couleur_index], -1)

                else:
                    prev_x, prev_y = 0, 0

                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Fusionner le dessin avec la caméra
        frame = cv2.addWeighted(frame, 0.7, canvas, 0.3, 0)

        # Afficher la couleur actuelle
        cv2.circle(frame, (w - 30, 30), 20, couleurs[couleur_index], -1)
        cv2.putText(frame, "Poing=Effacer | Pouce+Index=Couleur | Index=Dessiner",
                    (5, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

        cv2.imshow('Finger Draw', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
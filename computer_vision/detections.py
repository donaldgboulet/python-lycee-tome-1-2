import cv2
import mediapipe as mp

# Initialisation
mp_pose = mp.solutions.pose
mp_face = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
for i in range(30):
    cap.read()

with mp_pose.Pose(min_detection_confidence=0.7) as pose, \
     mp_face.FaceDetection(min_detection_confidence=0.7) as face, \
     mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # --- CORPS ---
        pose_results = pose.process(rgb)
        if pose_results.pose_landmarks:
            mp_draw.draw_landmarks(
                frame, pose_results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
                mp_draw.DrawingSpec(color=(0, 200, 0), thickness=2)
            )
            lm = pose_results.pose_landmarks.landmark

            # Noms des parties du corps
            parties = {
                "Nose":          mp_pose.PoseLandmark.NOSE,
                "L.Shoulder":    mp_pose.PoseLandmark.LEFT_SHOULDER,
                "R.Shoulder":    mp_pose.PoseLandmark.RIGHT_SHOULDER,
                "L.Elbow":       mp_pose.PoseLandmark.LEFT_ELBOW,
                "R.Elbow":       mp_pose.PoseLandmark.RIGHT_ELBOW,
                "L.Wrist":       mp_pose.PoseLandmark.LEFT_WRIST,
                "R.Wrist":       mp_pose.PoseLandmark.RIGHT_WRIST,
                "L.Hip":         mp_pose.PoseLandmark.LEFT_HIP,
                "R.Hip":         mp_pose.PoseLandmark.RIGHT_HIP,
                "L.Knee":        mp_pose.PoseLandmark.LEFT_KNEE,
                "R.Knee":        mp_pose.PoseLandmark.RIGHT_KNEE,
                "L.Ankle":       mp_pose.PoseLandmark.LEFT_ANKLE,
                "R.Ankle":       mp_pose.PoseLandmark.RIGHT_ANKLE,
            }

            for nom, point in parties.items():
                x = int(lm[point].x * w)
                y = int(lm[point].y * h)
                cv2.putText(frame, nom, (x + 5, y - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 100), 1)

        # --- VISAGE ---
        face_results = face.process(rgb)
        if face_results.detections:
            for detection in face_results.detections:
                bbox = detection.location_data.relative_bounding_box
                x1 = int(bbox.xmin * w)
                y1 = int(bbox.ymin * h)
                bw = int(bbox.width * w)
                bh = int(bbox.height * h)
                cv2.rectangle(frame, (x1, y1), (x1+bw, y1+bh), (255, 0, 0), 2)
                cv2.putText(frame, "Face", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # --- MAINS ---
        hand_results = hands.process(rgb)
        if hand_results.multi_hand_landmarks:
            FINGER_NAMES = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
            finger_tips = [4, 8, 12, 16, 20]

            for i, hand_landmarks in enumerate(hand_results.multi_hand_landmarks):
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                hand_label = hand_results.multi_handedness[i].classification[0].label
                label = "Right Hand" if hand_label == "Right" else "Left Hand"

                for j, tip_id in enumerate(finger_tips):
                    lm_h = hand_landmarks.landmark[tip_id]
                    x = int(lm_h.x * w)
                    y = int(lm_h.y * h)
                    cv2.putText(frame, FINGER_NAMES[j], (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)

                wrist = hand_landmarks.landmark[0]
                wx = int(wrist.x * w)
                wy = int(wrist.y * h)
                cv2.putText(frame, label, (wx - 30, wy - 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 100, 0), 2)

        # --- INFO en haut ---
        cv2.putText(frame, "Corps + Visage + Mains", (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow('Detection Complete', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
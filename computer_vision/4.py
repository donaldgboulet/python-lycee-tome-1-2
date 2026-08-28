import cv2

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

for i in range(30):
    cap.read()

ret, frame = cap.read()
if ret:
    cv2.imwrite("C:/Users/edgbo/photo_test.jpg", frame)
    print("Photo sauvegardée !")
else:
    print("Erreur - caméra non trouvée")

cap.release()
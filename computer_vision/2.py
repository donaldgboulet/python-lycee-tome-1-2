import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.circle(img, (200, 200), 100, (0, 255, 0), -1)
cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), 3)
cv2.putText(img, "OpenCV!", (120, 350), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
cv2.imshow("Test OpenCV", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
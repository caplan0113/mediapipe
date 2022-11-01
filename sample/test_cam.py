import cv2
import sys

cap = cv2.VideoCapture(int(sys.argv[1]))


while True:
	ret, frame = cap.read()
	cv2.imshow('camera', frame)
	key = cv2.waitKey(10)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindow()

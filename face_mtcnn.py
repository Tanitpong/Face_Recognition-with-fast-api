from mtcnn.mtcnn import MTCNN
import tensorflow
import cv2

cap = cv2.VideoCapture(0)
detector = MTCNN()
while 1 > 0:
        ret, frame = cap.read()
        Detected = detector.detect_faces(frame)
        print(Detected)

        
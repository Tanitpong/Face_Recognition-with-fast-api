from mtcnn import MTCNN
import cv2
img = cv2.cvtColor(cv2.imread(r"D:\[0]PyScript\Face_Recognition-with-fast-api\Face_Recognition-with-fast-api\train\Beeby\310852.jpg"), cv2.COLOR_BGR2RGB)
detector = MTCNN()
detector.detect_faces(img)

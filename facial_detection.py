import cv2
from matplotlib import pyplot as plt
import numpy as np

def main():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        detect_darkness(frame)
        face_detect = cv2.CascadeClassifier("harr_casscade_classifiers/haarcascade_frontalface_default.xml")
        shape = face_detect.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))

        rect_pos = []
        for (x, y, w, h) in shape:
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 4)
            rect_pos.append([x, y, w, h])
        if algorithm(rect_pos):
            print("Eyes detected, you may go through")
        else: print("No eyes detected, you may not go through")
        if not ret: raise Exception("No camera was detected")
        if cv2.waitKey(1) & 0xff == ord("q"): break

        cv2.imshow("Camera", frame)
    cam.release()
    cv2.destroyAllWindows()

def algorithm(rectangles) -> bool:
    import math
    if not len(rectangles) == 2: return False
    eye_1 = rectangles[0][:2]
    eye_2 = rectangles[1][:2]
    # distance between 2 lines
    dist = math.sqrt(math.pow(eye_2[0] - eye_1[0], 2) + math.pow(eye_2[1] - eye_1[1], 2))
    if dist <= 100:
        return True

    # size ratio
    square_1, square_2 = math.prod(eye_1), math.prod(eye_2)
    if square_1 > square_2 and square_2/square_1 >= 0.7:
        return True
    elif square_2 > square_1 and square_1/square_2 >= 0.7:
        return True

    return False



def detect_darkness(frame:np.ndarray):
    if np.average(frame) < 10:
        print("Scene is dark, please remove webcam or illuminate area.")

if __name__ == "__main__":
    main()
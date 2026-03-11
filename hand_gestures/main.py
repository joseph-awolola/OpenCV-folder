import math
import screen_brightness_control
import mediapipe as mp
import numpy as np
import cv2



mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2
)

def signal_1():
    if math.dist(i1, i2) <= math.dist(t1, i1):
        print("Signal 1 active")


def signal_2(pt_1:tuple, pt_2:tuple, ref:tuple):
    if math.dist(ref, pt_1) <= math.dist(pt_1, pt_2):
        print("Signal 2 active")

def signal_3(pt_1:tuple, pt_2:tuple, ref:tuple):
    if math.dist(ref, pt_1) <= math.dist(pt_1, pt_2):
        print("Signal 3 active")

def signal_4(pt_1:tuple, pt_2:tuple, ref:tuple):
    if math.dist(ref, pt_1) <= math.dist(pt_1, pt_2):
        print("Signal 4 active")



Draw = mp.solutions.drawing_utils
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    Process = hands.process(rgb_img)
    landmarkList = []

    if Process.multi_hand_landmarks:
        # detect handmarks
        for handlm in Process.multi_hand_landmarks:
            for _id, landmarks in enumerate(handlm.landmark):
                # store height and width of image
                height, width, color_channels = frame.shape

                # calculate and append x, y coordinates
                # of handmarks from image(frame) to lmList
                x, y = int(landmarks.x * width), int(landmarks.y * height)
                landmarkList.append([_id, x, y])

            # draw Landmarks
            Draw.draw_landmarks(frame, handlm,
                                mpHands.HAND_CONNECTIONS)


    if landmarkList:
        finger_coords = []

        # thumb tip 1
        t1 = landmarkList[4][1], landmarkList[4][2]
        # index tip
        i1 = landmarkList[8][1], landmarkList[8][2]
        # index 2
        i2 = landmarkList[7][1], landmarkList[7][2]
        m1 = landmarkList[12][1], landmarkList[12][2]
        r1 = landmarkList[16][1], landmarkList[16][2]
        p1 = landmarkList[20][1], landmarkList[20][2]
        if math.dist(i1, i2) >= math.dist(i1, t1):
            print("Signal 1 active")
        elif math.dist(i1, i2) >= math.dist(m1, t1):
            print("Signal 2 active")
        elif math.dist(i1, i2) >= math.dist(r1, t1):
            print("Signal 3 active")
        elif math.dist(i1, i2) >= math.dist(p1, t1):
            break

        frame = cv2.line(frame, t1, i1, (255, 0, 0), 2, 1)
        brightness_dist = math.dist(t1, i1)
        print(brightness_dist)
        if brightness_dist > 100:
            brightness_dist = 100
        screen_brightness_control.set_brightness(brightness_dist)
    frame = cv2.flip(frame, 1)
    cv2.imshow("Video Capture", frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cam.release()

import cv2
import numpy as np
import threading

def check_frame():
    for i in frame:
        for pixel in i:
            if pixel[1] > pixel[0] and pixel[1] > pixel[2] and (pixel[1] - pixel[2] >= 50 and pixel[1] - pixel[0] >= 50):
                print("This pixel is green")
                return


cam = cv2.VideoCapture("Images/WIN_20251008_20_03_24_Pro.mp4")
frames = cam.get(cv2.CAP_PROP_FRAME_COUNT)
fps:float = cam.get(cv2.CAP_PROP_FPS)

green_counter = 0
while True:
    try:
        _, frame = cam.read()
        cv2.imshow("image frame", frame)
        check_frame()
        green_counter += 1
    except cv2.error:
        break


    if cv2.waitKey(int((1/fps)*1000)) & 0xff == ord("q"): break


seconds_of_green = green_counter/fps
print(f"Green was visible for {seconds_of_green:2f} seconds")
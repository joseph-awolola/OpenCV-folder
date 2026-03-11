import cv2
from tkinter import *



def change_threshold(value):
    file = "Images/my pic.jpg"
    image = cv2.imread(file)
    edge_detect = cv2.Canny(image, value, 255)
    _, threshold_image = cv2.threshold(image, value, 255, cv2.THRESH_BINARY)
    cv2.imshow("page", threshold_image)
    print(value)
    if cv2.waitKey(0) & 0xFF == ord("q"): cv2.destroyAllWindows()



if __name__ == "__main__":
    window = Tk()

    scale = Scale(master=window, to=255)

    scale.pack()
    scale.bind("<ButtonRelease-1>", lambda event: change_threshold(scale.get()))
    window.mainloop()

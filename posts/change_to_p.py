with open("ml.txt","r") as f:
    text = f.read()
with open("ml.txt","w") as f:
    f.write(text.replace("\n","<p></p>"))

import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS)

import urllib.request
import cv2
import numpy as np
import imutils

url="http://192.168.43.1:8080/shot.jpg"     
while True:
    imgPath=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img=imutils.resize(img,width=450)
    cv2.imshow("cam feed",img)
    k=cv2.waitKey(1)                             # press esc to quit the camera feed
    if k==27:                                           # 27 represents the keyboard value of esc button
        break


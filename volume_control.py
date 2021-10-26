import cv2 as cv
import time
import mediapipe_module as mp
import math
import pyautogui as pg

wcam, hcam = 640, 480
cap = cv.VideoCapture(0)

cap.set(3,wcam)
cap.set(4,hcam)

ctime = 0
ptime = 0

detector = mp.HandTrack(max_detection_confidence=0.7)
# cv.namedWindow('image', cv.WINDOW_NORMAL)
# cv.setWindowProperty('image', cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

while True:
    _, image = cap.read()
    image = detector.findHands(image)
    lmlist = detector.findPosition(img = image, draw = False)
    if len(lmlist) != 0:
        # print(lmlist[4])
        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        cv.circle(image, (x1,y1), 10, (255,0,255), -1)
        cv.circle(image, (x2,y2), 10, (255,0,255), -1)
        cv.line(image, (x1,y1), (x2,y2), (255,0,255), 3)
        cx,cy = (x1+x2)//2, (y1+y2)//2
        cv.circle(image, (cx,cy), 10, (255,0,255), -1)

        length = math.hypot(x2 - x1, y2 - y1)
        if length < 80:
            cv.circle(image, (cx,cy), 10, (0,255,0), -1)
            pg.moveTo(cx*2.25,cy*3)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(image, str(int(fps)), (10,30),cv.FONT_HERSHEY_COMPLEX,1, (0,0,255),3)
    cv.imshow('image', image)
    if cv.waitKey(1)==27:
        break
cap.release()
cv.destroyAllWindows()


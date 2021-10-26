import cv2 as cv
import mediapipe as mp
import time


cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands()

ctime = 0
ptime = 0

while True:

    _, frame = cap.read()
    frame = cv.flip(frame, 1)
    imgRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c=frame.shape
                cx, cy = int(lm.x*w),int(lm.y*h)
                if id==5:
                    cv.circle(frame, (cx,cy),15, (255,255,0),-1)
            mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
    #frame rate calculation
    # ctime = time.time()
    # fps = 1/ctime-ptime
    # ptime = ctime
    # print(fps)


    cv.imshow("image", frame)
    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()
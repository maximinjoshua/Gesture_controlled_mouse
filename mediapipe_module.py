import cv2 as cv
import mediapipe as mp
import time

class HandTrack():
    def __init__(self,
                static_image_mode=False,
                max_num_hands=2,
                max_detection_confidence=0.5,
                min_tracking_confidence=0.5):

        self.static_iamge_mode = static_image_mode
        self.max_num_hands = max_num_hands
        self.max_detection_confidence  = max_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.mpHands = mp.solutions.hands
        self.mpDraw = mp.solutions.drawing_utils
        self.hands = self.mpHands.Hands(self.static_iamge_mode, self.max_num_hands,
                                         self.max_detection_confidence, self.min_tracking_confidence )
    
        
    def findHands(self, img):
            img = cv.flip(img, 1)
            imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            self.results = self.hands.process(imgRGB)

            if self.results.multi_hand_landmarks:
                for handLms in self.results.multi_hand_landmarks:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
            return img
    
    def findPosition(self, img, handNo=0, draw = False):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w),int(lm.y*h)
                lmlist.append([id, cx, cy])
                # if id==5:
                if draw == True:
                    cv.circle(img, (cx,cy),15, (255,0,255),-1)
        return lmlist

def main():
    ptime = 0
    ctime = 0
    cap = cv.VideoCapture(0)
    detector = HandTrack()
    while True:
        _, frame = cap.read()
        img = detector.findHands(frame)
        lmlist = detector.findPosition(img, draw = True)
        if len(lmlist) != 0:
            print(lmlist)
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv.putText(img, str(int(fps)), (10,70),cv.FONT_HERSHEY_COMPLEX,1, (0,0,255),3)
        cv.imshow('img',img)
        if cv.waitKey(1)==27:
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()


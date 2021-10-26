import cv2 as cv

capture = cv.VideoCapture(0)
_, image = capture.read()
previous = image.copy()


while True:
    _, image = capture.read()
    diff = cv.absdiff(image, previous)
    #image = cv.flip(image, 3)
    #image = cv.norm(image)
    _, diff = cv.threshold(diff, 32, 0, cv.THRESH_TOZERO)
    _, diff = cv.threshold(diff, 0, 255, cv.THRESH_BINARY)
    
    diff = cv.medianBlur(diff, 5)
    
    cv.imshow('video', diff)
    previous = image.copy()
    if cv.waitKey(1)==27:
        break
    
capture.release()
cv.destroyAllWindows() 


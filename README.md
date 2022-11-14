# Gesture controlled mouse

Run aicontrolledmouse.py and a window will open showing your webcam video feed
```
python aicontrolledmouse.py
```
![Picture1](https://user-images.githubusercontent.com/58840936/201737313-563836fa-261d-4571-a156-b281612f0e14.png)

Use the gesture in the image above to control your computer cursor with your hand. Gesture control does not work outside the box drawn on the video. So make sure that you don't go outside the box. The region within the box is enough to reach the ends of your display with your cursor. The hand movement has been restricted only within the box because the entire hand has to be on the video frame for the hand to be detected by mediapipe.

Extend your middle finger and touch the tip of the index finger to click.

Tuck in your index and middle fingers and extend your thumb to toggle.

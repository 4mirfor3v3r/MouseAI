import autopy.screen
import mouse
import keyboard
import cv2
import numpy as np
import HandTrackingModule as htm
import time

########################
wCam, hCam = 640, 480
frameR = 100
smoothening = 5
########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, wCam)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()
print(wScr, hScr)

STATE_POINTER = "Pointer"
STATE_PRESS_LEFT = "Left Pressed"
STATE_CLICK_LEFT = "Left Clicked"
STATE_PRESS_RIGHT = "Right Pressed"
STATE_CLICK_RIGHT = "Right Pressed"
MOUSE_STATE = "Pointer"

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:
        # forefinger
        x1, y1 = lmList[8][1:]
        # middle finger
        x2, y2 = lmList[12][1:]
        # thumb
        F_THUMB_X, F_THUMB_Y = lmList[4][1:]
        # little finger
        F_LITTLE_X, F_LITTLE_Y = lmList[20][1:]

        # print(x1,y1,x2,y2)
        fingers = detector.fingersUp()
        # print(fingers)

        # if fingers[0]==1 and fingers[1] == 1:
        #     length, img, lineInfo = detector.findDistance(4, 8, img)
        #     if length < 40:
        #         cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
        #         autopy.mouse.click()
        if fingers[1] == 1 or fingers[2]==1:
            cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

            length, img, lineInfo = detector.findDistance(8, 12, img)
            if fingers[2]==0 and MOUSE_STATE!=STATE_PRESS_LEFT:
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, down=False)
                if MOUSE_STATE != STATE_CLICK_LEFT:
                    cv2.circle(img, (x2, y2), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click(autopy.mouse.Button.LEFT)

                MOUSE_STATE = STATE_CLICK_LEFT
            elif length > 70:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                if MOUSE_STATE != STATE_PRESS_LEFT:
                    autopy.mouse.toggle(autopy.mouse.Button.LEFT,down = True)
                MOUSE_STATE = STATE_PRESS_LEFT
            elif fingers[4]==0:
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, down=False)
                if MOUSE_STATE != STATE_CLICK_RIGHT:
                    cv2.circle(img, (F_LITTLE_X, F_LITTLE_Y), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click(autopy.mouse.Button.RIGHT)
                MOUSE_STATE = STATE_CLICK_RIGHT
            else:
                MOUSE_STATE = STATE_POINTER
                autopy.mouse.toggle(autopy.mouse.Button.LEFT, down=False)
        print(MOUSE_STATE)


        # click center finger
        # if fingers[1] == 1 and fingers[2] == 1:
        #     length, img, lineInfo = detector.findDistance(8, 12, img)
        #     if length < 40:
        #         cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
        #         autopy.mouse.click()

        # click thumb left
        # if fingers[0] == 1:
        #     length, img, lineInfo = detector.findDistance(8, 12, img)
        #     cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
        #     # autopy.mouse.click()
        #
        # if fingers[1] == 1 and fingers[2] == 1:
        #     length, img, lineInfo = detector.findDistance(8, 12, img)
        #     if length < 40:
        #         cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
        #         # autopy.mouse.click()

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Mouse Proto 2", img)
    cv2.waitKey(1)

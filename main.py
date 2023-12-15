import cv2
import numpy as nm
import autopy
import handtracking as htm
import time

###size the webcam
wcam, hcam =640,480
frameR = 150

###
plocx,plocy = 0,0
clocx,clocy = 0,0
smoothning = 7


cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)
pTime = 0                     ##11
detector = htm.handDetector(maxHands=1)
wscr,hscr = autopy.screen.size()
#print(wscr,hscr)

while True:
    # 1. find the hand landmark
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    #print(lmList)   2d list of index of all 21 node form on palm in which 8th and 12th are index and middle
    # 2. get the tip of index and middle finger
    if len(lmList)!=0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        #print(x1,x2,y1,y2)   #this print the tip coordinate of index and middle finger

    # 3. check which finger is up
        fingers = detector.fingersUp()
        #print(fingers)      # print which finger is open and close
    # 4. only index finger i.e moving mode
        cv2.rectangle(img, (frameR, frameR), ((wcam - frameR), (hcam - frameR)), (255, 23, 14), 2)
        if fingers[1]==1 and fingers[2]==0:
           # print("click")

    # 5. convert coordinate as per screen size

            x3 = nm.interp(x1,(frameR,wcam-frameR),(0,wscr))
            y3 = nm.interp(y1,(frameR,hcam-frameR ),(0,hscr))
    # 6. smoothen value
            clocx = plocx + (x3-plocx)/ smoothning
            clocy = plocy + (y3-plocy)/ smoothning
    # 7. move mouse
            autopy.mouse.move(wscr-clocx, clocy)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            plocx, plocy = clocx, clocy
    # 8. check if both index and middle finger sre up then it is clicking mode
        # for left click
        # 9. find the distance between fingers
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8,12,img)
           # print(length)
        # 10. click mouse if distance is short
            if length < 40:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                autopy.mouse.click(autopy.mouse.Button.LEFT)
                cv2.waitKey(500)

        # for right click
        elif fingers[1] == 1 and fingers[2]==0 and fingers[4] == 1 :

                autopy.mouse.click(autopy.mouse.Button.RIGHT)
                cv2.waitKey(800)


    # 11. frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    # 12. display
    cv2.imshow("Image",img)

    # 13. quit
    if cv2.waitKey(1) == ord('q'):
        break

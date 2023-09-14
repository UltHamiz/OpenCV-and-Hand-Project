import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)


while cap.isOpened():

    try:
        ret, img = cap.read()

        ri = img[100:300, 100:300]
        cv2.rectangle(img,(100,100),(300,300),(0,255,0),1)

        imgHSV = cv2.cvtColor(ri, cv2.COLOR_BGR2HSV)
        lower = np.array([0, 48, 90],dtype = "uint8")
        upper = np.array([20, 255, 255],dtype = "uint8")

        skinMask = cv2.inRange(imgHSV, lower, upper)

        blurredMask = cv2.blur(skinMask, (2,2))
        ret,thresh = cv2.threshold(blurredMask,0,255,cv2.THRESH_BINARY)

        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt = max(contours, key=lambda x: cv2.contourArea(x))
        hull = cv2.convexHull(cnt)

        cv2.drawContours(ri, [cnt], -1, (0, 255, 0), 3)
        cv2.drawContours(ri, [hull], -1, (0, 255, 255), 2)

        # rect = cv2.minAreaRect(cnt)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        # cv2.drawContours(ri, [box], 0, (0, 0, 255), 2)

        areaHull = cv2.contourArea(hull)
        areaContour = cv2.contourArea(cnt)

        areaRatio = round(((areaHull-areaContour)/areaContour)*100,2)
        # print(areaRatio)

        perimeter = cv2.arcLength(cnt, True)
        # print(perimeter)


        cv2.putText(img, str(areaRatio), (0, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)

        hullD = cv2.convexHull(cnt, returnPoints=False)
        defects = cv2.convexityDefects(cnt,hullD)

        l = 0

        for i in range(defects.shape[0]):
            s, e, f, d = defects[i][0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])

            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])** 2 + (far[1] - start[1])** 2)
            c = math.sqrt((end[0] - far[0])** 2 + (end[1] - far[1])** 2)

            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))

            if angle <= math.pi/2 :
                l += 1
                cv2.circle(ri,far,4,[0,0,255],-1)
        l += 1

        font = cv2.FONT_HERSHEY_SIMPLEX
        if l == 1:
            if areaContour < 2000:
                cv2.putText(img, 'No Hand', (100, 50), font, 1, (0, 0, 255), 3)
            else:
                if areaRatio < 6.5:
                    cv2.putText(img, 'A', (100, 50), font, 1, (0, 0, 255), 3)
                elif areaRatio < 10:
                    cv2.putText(img, 'Zero', (100, 50), font, 1, (0, 0, 255), 3)
                else:
                    cv2.putText(img, 'One', (100, 50), font, 1, (0, 0, 255), 3)

        elif l == 2:
            if areaRatio < 45:
                cv2.putText(img, 'Two', (100, 50), font, 1, (0, 0, 255), 3)
            else:
                cv2.putText(img, 'C', (100, 50), font, 1, (0, 0, 255), 3)

        elif l == 3:
            if areaRatio < 68:
                cv2.putText(img, 'Three', (100, 50), font, 1, (0, 0, 255), 3)
            else:
                cv2.putText(img, 'I Love You', (100, 50), font, 1, (0, 0, 255), 3)

        elif l == 4:
            cv2.putText(img, 'Four', (100, 50), font, 1, (0, 0, 255), 3)

        elif l == 5:
            cv2.putText(img, 'Five', (100, 50), font, 1, (0, 0, 255), 3)
        elif l > 6:
            cv2.putText(img, 'Reposistion', (100, 50), font, 1, (0, 0, 255), 3)

        cv2.putText(img,str(l),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

        cv2.imshow("Main", img)
        cv2.imshow("Mask", skinMask)
        cv2.imshow("HSV",imgHSV)
    except:
        pass
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

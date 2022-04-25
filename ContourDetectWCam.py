import cv2
import numpy as np
# Contour/Shape Detection  (He uses stacking function, not necessary)

def getContours(img):
    # img, returns extreme out contours, compressed value or all values for contours
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours: # Loops through all values in contours
        area = cv2.contourArea(cnt)
        print(area)
        # Check for minimum area with a given threshold
        if area > 500:
            # img draw on, cnt (from loop), contour index (-1 for all), color, thickness
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # calculate the curve length to approx corners of shape (True statements, bc shapes are closed)
            peri = cv2.arcLength(cnt,True)
            print(peri)
            # approximate the number of corners
            approx = cv2.approxPolyDP(cnt,0.02*peri, True) # contour,resolution (mess w/ this)
            print(len(approx)) # outputs number points of corners, approx is a list of corners, getting length of list
            objCor = len(approx)
            # Create bounding box around detected object, cords of box
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:         # Categorizing Shapes
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio <1.05:
                    objectType = "Square"
                else:
                   objectType = "Rect"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType ="None"

            # Draws box around for each contour based on points from approx
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2) # Bounding box useful for getting shape info
            # puts text over shape w/name,
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)




# path = "Resources/shapes.png"
# img = cv2.imread(path)
# imgContour = img.copy()

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,720)
cap.set(4,1280)
cap.set(10,100)

while True:
    success, img = cap.read()
    imgContour = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContours(imgCanny)

    cv2.imshow("Contour", imgContour)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

# imgBlank = np.zeros_like(img)

# cv2.imshow("Orignal", img)
# cv2.imshow("Gray", imgGray)
# cv2.imshow("Blur", imgBlur)
# cv2.imshow("Canny", imgCanny)

cap.release()
cv2.destroyAllWindows()
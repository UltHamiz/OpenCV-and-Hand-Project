import cv2
import numpy as np
# Color Detection

def empty(a): # empty function
    pass


path = "Resources/0_y35KUbiwN5PlSmF4.jpg"
cv2.namedWindow("TrackBars") # Creating and sizing a window for trackbars
cv2.resizeWindow("TrackBars",640,240)
# Trackbar name, window name its on, initial value, max value (Hue 0-179), function that runs every time trackbar changes
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",19,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",110,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",240,255,empty)
cv2.createTrackbar("Val Min","TrackBars",15,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #Converts Colors to HSV
    # Gets tracks bars so they can be changed
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    # using values to filter image to get particular color in image
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    # filter out image of color input
    mask = cv2.inRange(imgHSV,lower, upper) # img, lower, upper limit (matrix)
    # Creating new image based on mask, with color
    imgResult = cv2.bitwise_and(img,img,mask=mask) # old img, new image, mask applied

    cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    # cv2.imshow("Image Result", imgResult)
    cv2.waitKey(1)
import cv2
import numpy as np
#Basic Functions

img = cv2.imread("Resources/0_y35KUbiwN5PlSmF4.jpg")
kernel = np.ones((5,5),np.uint8) # 24:45

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Grayscale conversion
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # Blurs Image, 7,7 is a Ksize (how blurry), must be odd
imgCanny = cv2.Canny(img, 150, 200)  # Image line detector
# 23:30, kernel is a matrices, which is gotten from numpy, used for line thickness
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1) # Does the operation of Dialation

cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)

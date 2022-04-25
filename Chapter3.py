import cv2
import numpy as np
# Image Resizing and cropping

img = cv2.imread("Resources/lambo.png")
print(img.shape)
# Gives Dimensions of img, (height, width, color channels)

imgResize = cv2.resize(img,(300,200))
# (width, height)
print(imgResize.shape)

imgCropped = img[0:200, 200:500] # height,width

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)


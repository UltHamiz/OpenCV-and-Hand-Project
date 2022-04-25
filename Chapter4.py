# import cv2
# import numpy as np
# #Shapes and Texts (on top of images)
#
# # Matrix with zero value, 512 by 512 dimensions, 3 color channels (RGB), np.uint gives values from 0-255
# img = np.zeros((512,512,3),np.uint8)
# # print(img)
# # img.shape for dimensions, img for matrix
#
# # img[200:300, 100:300]= 255,0,0
# # [h,w], : means whole img , makes img blue
#
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# # img, start, end, color, thickness
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
# # img, start, end, color , thickness/fill function (cv2.FILLED)
# cv2.circle(img,(400,50),30,(255,255,0),5)
# # img, center, radius
# cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)
# # img, text, origin, font, scale, color, thickness
#
# cv2.imshow("Image", img)
# cv2.waitKey(0)


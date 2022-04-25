import cv2
# Reading images, videos, and webcam

# Image Import
# img = cv2.imread("Resources/lena.jpg")
#
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# Video Import
# cap = cv2.VideoCapture("Resources/testVideo.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# Webcam Import

cap = cv2.VideoCapture(0)
# cap.set(3,720) # width
# cap.set(4,1280) # height
# cap.set(10,100) # brightness


while True:
    success, img = cap.read()
    ri = img[100:300, 100 :300]

    # grayScale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Gray Video", grayScale)
    cv2.imshow("Video", img)
    cv2.imshow("ri", ri)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

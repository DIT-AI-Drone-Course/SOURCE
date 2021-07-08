import cv2

img = cv2.imread('drone_pic.JPG')
c

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 250, 10)
cv2.imshow('image',img)

k = cv2.waitKey(0)
if k == 27: # esc key
    cv2.destroyAllWindow()
elif k == ord('s'): # 's' key
    cv2.imwrite('testgray.png',img)
    cv2.destroyAllWindow()
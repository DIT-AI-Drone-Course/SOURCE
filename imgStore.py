import cv2

img = cv2.imread('./opencv03.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: # esc key
    cv2.destroyAllWindow()
elif k == ord('s'): # 's' key
    cv2.imwrite('testgray.png',img)
    cv2.destroyAllWindow()
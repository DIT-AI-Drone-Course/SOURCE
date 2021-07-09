import cv2
img = cv2.imread('./drone01.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)

k = cv2.waitKey(0)

if k == 27: # esc key
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('testgray.png',img)
elif k == ord('r'):
    cv2.resize(img, (320, 240))

cv2.destroyAllWindows()

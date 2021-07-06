import cv2

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print('width: {}, height : {}'.format(cap.get(3), cap.get(4)))

while True:
    ret, frame = cap.read()

    if ret:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('video', gray)
        cv2.imshow('video', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # 27 -> ESC
            break
    else:
        print('error')

cap.release()
cv2.destroyAllWindows()
import cv2

cap = cv2.VideoCapture(0)
w = cap.get(3)
h = cap.get(4)
print("w = ", w)
print("h = ", h)

while(cap.isOpened()):
    ret, img = cap.read()
    if ret:
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 1.2 : scale factor,  8 : minNeighbors
        faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cx = x + w // 2
            cy = y + h // 2
            area = w * h
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

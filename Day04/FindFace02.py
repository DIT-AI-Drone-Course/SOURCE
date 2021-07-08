import cv2

cap = cv2.VideoCapture(0)

def findFace(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy),10,(0,255,0), 6)
        myFaceListC.append([cx,cy])
        myFaceListArea.append(area)
        # print(myFaceListC)
    if len(myFaceListArea) != 0:
        i= myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]

while True:
    # _, img = cap.read()
    ret, img = cap.read()
    if ret:
        img, info = findFace(img)
        print(info[0], " ", info[1])
        cv2.imshow("cam", img)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()

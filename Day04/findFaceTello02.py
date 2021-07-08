import cv2
from djitellopy import tello

tello = tello.Tello()
tello.connect()
battery_level = tello.get_battery()
print(battery_level)
tello.streamon()

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
   img = tello.get_frame_read().frame
   img = cv2.resize(img, (360, 240))

   img, info = findFace(img)
   cv2.imshow('frame',img)
   if cv2.waitKey(5) & 0xFF == ord('q'):
       break

# Release everything if job is finished
# cap.release()
# out.release()
cv2.destroyAllWindows()

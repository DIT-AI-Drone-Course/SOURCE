import cv2
from djitellopy import tello

tello = tello.Tello()
tello.connect()
battery_level = tello.get_battery()
print(battery_level)
tello.streamon()

w, h = 360, 240
fbRange = [6200, 6800]
fb = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("../day04/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 5)

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

    if len(myFaceListArea) != 0:
        i= myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i],myFaceListArea[i]]
    else:
        return img, [[0,0],0]

while True:
   img = tello.get_frame_read().frame
   img = cv2.resize(img, (360, 240))
   img, info = findFace(img)

   # info[1] -> area
   if info[1] > fbRange[0] and info[1] < fbRange[1]:
       fb = 0
   elif info[1] > fbRange[1]:
       fb = -20
   elif info[1] < fbRange[0] and info[1] != 0:
       fb = 20
   if info[0][0] == 0:  # info[0][0] -> x
       speed = 0
       # error = 0
   print(fb)
   tello.send_rc_control(0, fb, 0, 0)

   cv2.imshow('frame',img)
   # print(info[0], info[1])

   k = cv2.waitKey(10) & 0xFF
   if k == ord('q'):
       tello.land()
       break
   elif k == ord('t'):
       tello.takeoff()
       tello.move_up(30)

tello.streamoff()
cv2.destroyAllWindows()

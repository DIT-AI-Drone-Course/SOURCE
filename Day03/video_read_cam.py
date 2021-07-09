import cv2

# cap = cv2.VideoCapture(0)
# if cap.isOpened():
#     w = cap.get(3)
#     h = cap.get(4)
#     print('width: {}, height : {}'.format(w, h))

from djitellopy import tello
import cv2
import time

tello = tello.Tello()
tello.connect()

battery_level = tello.get_battery()
print(battery_level)

time.sleep(2)
tello.streamon()

# read a single image from the Tello video feed
# frame_read = tello.get_frame_read()

while True:
    frame_read = tello.get_frame_read()
    # frame = frame_read.frame
    gray = cv2.cvtColor(frame_read.frame, cv2.COLOR_BGR2GRAY)
    # r_frame = cv2.resize(frame, (320 * 2, 240 * 2))
    cv2.imshow('video', gray)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    elif k == ord('t'):
        tello.takeoff()
        tello.move_up(60)
        tello.rotate_clockwise(360)
    elif k == ord('l'):
        tello.land()
        tello.streamoff()

# cap.release()
tello.streamoff()
cv2.destroyAllWindows()
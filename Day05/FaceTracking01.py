import numpy as np
from djitellopy import tello
import cv2

tello = tello.Tello()
tello.connect()
battery_level = tello.get_battery()
print(battery_level)
tello.streamon()

# # Video save
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('out.avi',fourcc, 20.0, (cap.get(cv2.CAP_PROP_FRAME_HEIGHT),cv2.CAP_PROP_FRAME_WIDTH))

def adjust_tello_position(offset_x, offset_y, offset_z):
    """
    Adjusts the position of the tello drone based on the offset values given from the frame
    :param offset_x: Offset between center and face x coordinates
    :param offset_y: Offset between center and face y coordinates
    :param offset_z: Area of the face detection rectangle on the frame
    """
    if not -90 <= offset_x <= 90 and offset_x != 0:
        if offset_x < 0:
            tello.rotate_counter_clockwise(10)
        elif offset_x > 0:
            tello.rotate_clockwise(10)

    if not -70 <= offset_y <= 70 and offset_y != -30:
        if offset_y < 0:
            tello.move_up(20)
        elif offset_y > 0:
            tello.move_down(20)

    if not 15000 <= offset_z <= 30000 and offset_z != 0:
        if offset_z < 15000:
            tello.move_forward(20)
        elif offset_z > 30000:
            tello.move_back(20)


face_cascade = cv2.CascadeClassifier('../day04/haarcascade_frontalface_default.xml')
frame_read = tello.get_frame_read()


# Video save
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi',fourcc, 20.0, (960, 720))

tello.takeoff()
tello.move_up(30)

while True:
    frame = frame_read.frame

    cap = tello.get_video_capture()
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    # Calculate frame center
    center_x = int(width / 2)
    center_y = int(height / 2)

    # Draw the center of the frame
    cv2.circle(frame, (center_x, center_y), 10, (0, 255, 0), 6)

    # Convert frame to grayscale in order to apply the haar cascade
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, minNeighbors=5)

    # If a face is recognized, draw a rectangle over it and add it to the face list
    face_center_x = center_x
    face_center_y = center_y
    z_area = 0

    for face in faces:
        (x, y, w, h) = face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

        face_center_x = x + int(h / 2)
        face_center_y = y + int(w / 2)
        z_area = w * h

        cv2.circle(frame, (face_center_x, face_center_y), 10, (0, 0, 255), 6)

    # Calculate recognized face offset from center
    offset_x = face_center_x - center_x
    # Add 30 so that the drone covers as much of the subject as possible
    offset_y = face_center_y - center_y - 30

    cv2.putText(frame, f'[{offset_x}, {offset_y}, {z_area}]', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2,
               cv2.LINE_8)
    adjust_tello_position(offset_x, offset_y, z_area)

    # Display the resulting frame
    # out.write(frame)
    cv2.imshow('Tello detection...', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        tello.land()
        break
    elif key == ord('t'):
        tello.takeoff()
        tello.move_up(30)

# Stop the BackgroundFrameRead and land the drone
tello.end()
cv2.destroyAllWindows()
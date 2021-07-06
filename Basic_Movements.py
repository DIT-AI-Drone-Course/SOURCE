from djitellopy import Tello
from time import sleep

me = Tello()
me.connect()
print(me.get_battery())
me.takeoff()
me.send_rc_control(0, 50, 0, 0) # updown 50
sleep(2)
me.send_rc_control(0, 0, 0, 30) # yaw 30
sleep(2)
me.send_rc_control(0, 0, 0, 0)
me.land()


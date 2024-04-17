# (Advanced) Lover implementation
from unifr_api_epuck import wrapper

MY_IP = '192.168.2.201'  # change robot number
robot = wrapper.get_robot(MY_IP)

NORM_SPEED = 1.5
MAX_PROX = 100
a = 1
b = 1
c = 2
d = 3

robot.init_sensors()
robot.calibrate_prox()

#INFINITE LOOP
while robot.go_on():
    prox_values = robot.get_calibrate_prox()
    proxR = (a * prox_values[0] + b * prox_values[1] + c * prox_values[2] + d * prox_values[3]) / (a + b + c + d)
    proxL = (a * prox_values[7] + b * prox_values[6] + c * prox_values[5] + d * prox_values[4]) / (a + b + c + d)
    dsR = (NORM_SPEED * proxR) / MAX_PROX
    dsL = (NORM_SPEED * proxL) / MAX_PROX
    speedR = (NORM_SPEED - dsR)
    speedL = (NORM_SPEED - dsL)
    robot.set_speed(speedL, speedR)
    
robot.clean_up()

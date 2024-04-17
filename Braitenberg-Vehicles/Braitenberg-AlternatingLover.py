# Alternating Lover-Explorer implementation
from unifr_api_epuck import wrapper

import time

MY_IP = '192.168.2.211'  # change robot number
robot = wrapper.get_robot(MY_IP)


NORM_SPEED = 1.5
MAX_PROX = 100
a = 1
b = 1
c = 2
d = -2
lover = True

robot.init_sensors()
robot.calibrate_prox()

# lets save all the speed in a list
speed_median = [1.5] * 30
i = 0

robot.enable_all_led()

# Starts with lover mode
while robot.go_on():
	prox_values = robot.get_calibrate_prox()
	proxR = (a * prox_values[0] + b * prox_values[1] + c * prox_values[2] + d * prox_values[3]) / (a + b + c + d)
	proxL = (a * prox_values[7] + b * prox_values[6] + c * prox_values[5] + d * prox_values[4]) / (a + b + c + d)
	dsR = (NORM_SPEED * proxR) / MAX_PROX
	dsL = (NORM_SPEED * proxL) / MAX_PROX
	speedR = (NORM_SPEED - dsR)
	speedL = (NORM_SPEED - dsL)
	robot.set_speed(speedR, speedL)
	if (lover == True):
		robot.set_speed(speedL, speedR)
	else:
		robot.set_speed(speedR, speedL)
	if (i == 30):
		i = 0
	speed_median[i] = (speedL + speedR) / 2
	i = i + 1
	
	# Switch between Lover and Explorer
	if (sum(speed_median) / 30 < 0.1 and sum(speed_median) / 30 > -0.1):
		lover = False
		robot.disable_all_led()
	if (sum(speed_median) / 30 < 1.5 and sum(speed_median) / 30 > 1.3):
		lover = True
		robot.enable_all_led()
   	
robot.clean_up()

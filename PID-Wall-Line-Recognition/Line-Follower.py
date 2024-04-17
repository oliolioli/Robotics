# run the code to generate IR sensor data 
from unifr_api_epuck import wrapper
import signal
import time
import sys

LEFT = 2
MID = 1
RIGHT = 0

counter = 0

state = "forward"

MY_IP = '192.168.2.207'

robot = wrapper.get_robot(MY_IP)

robot.init_ground()

def signal_handler(sig, frame):
	robot.clean_up()
	exit()

def turn_right():
    robot.set_speed(3, 0)
        
def turn_left():
    robot.set_speed(0, 3)

signal.signal(signal.SIGINT, signal_handler)

while robot.go_on():
    gs = robot.get_ground()
    if (state == "turn_right"):
        turn_right()
        counter += 1
    elif (state == "turn_left"):
        turn_left()
        counter += 1
    elif (gs[MID] < 500 and gs[LEFT] < 500 and gs[RIGHT] < 500) :
        state = "turn_left"
    elif (gs[MID] > 500 and gs[LEFT] > 500 and gs[RIGHT] > 500) :
        state = "turn_right"
    elif (gs[MID] > 500 and gs[LEFT] < 500) :
        robot.set_speed(2, 0)
    elif (gs[LEFT] > 500 and gs[RIGHT] < 500) :
        robot.set_speed(0, 2)
    else : 
        robot.set_speed(2, 2)
        
    if (counter >= 100) :
        counter = 0
        state = "forward"
      
robot.clean_up()

from unifr_api_epuck import wrapper
import sys, random, signal
import numpy as np

def handler(signum, frame):
    robot.clean_up()

def compare(msg, r, g, b):
    msg = msg.split(" ")
    msgr = int(msg[0])
    msgg = int(msg[1])
    msgb = int(msg[2])
    if (msgr == r and msgg == g and msgb == b):
        return (True)
    else:
        return (False)

if __name__ == "__main__":
    """
    if arguments in the command line --> IRL
    no arguemnts --> use Webots
    """
    ip_addr = 'NO_ARGS'
    if len(sys.argv) == 2:
        ip_addr = sys.argv[1]
    
    robot = wrapper.get_robot(ip_addr)

    signal.signal(signal.SIGINT, handler)   
    
    NORM_SPEED = 1.2
    MAX_PROX = 250

    robot.init_sensors()
    robot.calibrate_prox()
    robot.initiate_model()
    robot.init_client_communication()

    robot.init_camera("img")
    
    stepcounter = 0
    n = 10
    
    while robot.go_on():
        red = 0
        green = 0
        blue = 0

        if stepcounter % n == 0 :
            robot.init_camera()
        if stepcounter % n == 1 :
            img = np.array(robot.get_camera())
            detections = robot.get_detection(img)
            if (len(detections) > 0):
                for object in detections:
                    if (object.label == "Red Block"):
                        red += 1
                    elif (object.label == "Green Block"):
                        green += 1
                    elif  (object.label == "Blue Block"):
                        blue += 1
            else:
                MSG = ""
        if (red != 0 or green != 0 or blue != 0):
            MSG = str(red) + str(green) + str(blue)
            robot.send_msg(MSG)
        stepcounter += 1
        
        if (robot.has_receive_msg()):
            received = robot.receive_msg()
            if (received == MSG):
                print(received)
                robot.enable_led(5, 100, 0, 0)
        else:
            robot.disable_all_led()
        
        # get IR sensor values
        prox = robot.get_calibrate_prox()
      
        # behaviours: compute speed according to prox values and current state 
        prox_left = (4 * prox[7] + 2 * prox[6] + prox[5]) / 7
        prox_right = (4 * prox[0] + 2 * prox[1] + prox[2]) / 7

        ds_left = (NORM_SPEED * prox_left) / MAX_PROX
        ds_right = (NORM_SPEED * prox_right) / MAX_PROX

        speed_left = NORM_SPEED - ds_right
        speed_right = NORM_SPEED - ds_left        
                        
        # set speed
        robot.set_speed(speed_left, speed_right)

    robot.clean_up()

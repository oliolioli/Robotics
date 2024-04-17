from unifr_api_epuck import wrapper
import os
import numpy as np

# connect to robot
MY_IP = '192.168.2.168'
robot = wrapper.get_robot(MY_IP)

# initiate model recognition and camera
robot.initiate_model()
robot.init_camera("img")

#wait 3 seconds
robot.sleep(3)

# calculate mean of the last 40 heights and widths
meanHList = [0] * 40
meanWList = [0] * 40
meanXCenterList = [0] * 40
i = 0

#step = 0
while robot.go_on():

    i += 1
    if i % 4:
        colors = np.array(robot.get_camera())
        detections = robot.get_detection(colors,0)
        
        [r,g,b] = colors

   
    if(len(detections) > 0):
        # only do all the calculations when we detect something...
        for item in detections:
            # ... and it is a red block
            if (item.label == "Red Block"):

                # save every value for calculating the mean
                meanWList[i] = int(item.width)
                meanHList[i] = int(item.height)
                meanXCenterList[i] = int(item.x_center)
                
                # calculate the mean of the lists (heigth and width)
                meanW = np.mean(meanWList)
                meanH = np.mean(meanHList)
                meanXCenter = np.mean(meanXCenterList)
                
                # print some information
                print("mean Height = " + str(meanH))
                print("mean Width = " + str(meanW))
                print("mean XCenter = " + str(meanXCenter))
                      
                # mainting the distance - worked robust with robot n° 4200
                constMinHeight = 80           
                constMaxHeight = 100           
                constMinWidth = 150           
                constMaxWidth = 165           
                
                
                # if distance ok, stay
                if ((constMinHeight < meanH and meanH < constMaxHeight) or (constMinWidth < meanW and meanW < constMaxWidth)):
                    print("Height and width ok - correct position")
                    ds_backandforth = 0
                # too far away, forward and love 
                elif ((meanH < constMinHeight) and (meanW < constMinWidth)):
                    print("Forward")
                    ds_backandforth = 1
                # too near, go back    
                else:
                    print("Backward")
                    ds_backandforth = -0.8
                    
                # if mean of item.x_center < 90 (plus margin)  block is on left side 
                if (meanXCenter < 80):
                    print("Block on left")
                    ds_left = -0.2
                    ds_right = 0.2
                # or on the right side
                elif (meanXCenter > 100):
                    print("Block on right")
                    ds_left = 0.2
                    ds_right = -0.2
                else:
                    print("Block in front")
                    ds_left = 0
                    ds_right = 0

                # calculate the speed of every wheel (with correction)
                speed_left  = ds_backandforth + ds_left
                speed_right = ds_backandforth + ds_right

                # move the robot into the correct direction 
                robot.set_speed(speed_left, speed_right)
                

    else:
        # if nothing is detected: stop robot
        print("Nothing in sight, stop robot")                            
        robot.set_speed(0,0)

    if (i == 39):
        i = 0

robot.clean_up()

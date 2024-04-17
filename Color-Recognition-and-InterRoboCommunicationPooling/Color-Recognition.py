# run the cell to record images
from unifr_api_epuck import wrapper
import os
import numpy as np


# create directory
try: 
    os.mkdir("./images") 
except OSError as error: 
    print(error)  

MY_IP = '192.168.2.168'
robot = wrapper.get_robot(MY_IP)

robot.init_camera('./images') # define your working directory for storing images (do not forget to create it)

robot.sleep(3)

#Tells wether the robot detected the color or not
red_on = False
green_on = False
blue_one = False

#Light the given leds in nbr[] to the given RGBs
def light_leds(nbr, r, g, b):
    for i in nbr:
        robot.enable_led(i, r, g, b)

#Light up the robot depending on which colors are detected
def light_robot():
    if (red_on and not green_on and not blue_on):
        light_leds([1, 3, 5, 7], 100, 0, 0)
    elif (not red_on and green_on and not blue_on):
        light_leds([1, 3, 5, 7], 0, 100, 0)
    elif (not red_on and not green_on and blue_on):
        light_leds([1, 3, 5, 7], 0, 0, 100)
    elif (red_on and green_on and not blue_on):
        light_leds([1, 3], 100, 0, 0)
        light_leds([5, 7], 0, 100, 0)
    elif (red_on and not green_on and blue_on):
        light_leds([5, 7], 100, 0, 0)
        light_leds([1, 3], 0, 0, 100)
    elif (not red_on and green_on and blue_on):
        light_leds([5, 7], 0, 100, 0)
        light_leds([1, 3], 0, 0, 100)
    else:
        light_leds([3], 100, 0, 0)
        light_leds([5], 0, 100, 0)
        light_leds([7], 0, 0, 100)
 
 #Checks wether the square of 10x10 starting from x and y is blue or not (blue value is higher of 30 at least than red and green)   
def check_blue(x, y, r, g, b):
    for i in range(10):
        for j in range(10):
            if (y+i > 119 or x+j > 159):
                return (False)
            if (b[y+i][x+j] < r[y+i][x+j] + 30 or b[y+i][x+j] < g[y+i][x+j] + 30):
                return (False)
    return (True)

#Checks wether the square of 10x10 starting from x and y is green or not (green value is higher of 15 at least than red and blue)
def check_green(x, y, r, g, b):
    for i in range(10):
        for j in range(10):
            if (y+i > 119 or x+j > 159):
                return (False)
            if (g[y+i][x+j] < r[y+i][x+j] + 15 or g[y+i][x+j] < b[y+i][x+j] + 15):
                return (False)
    return (True)

#Checks wether the square of 10x10 starting from x and y is red or not (red value is higher of 45 at least than blue and green)
def check_red(x, y, r, g, b):
    for i in range(10):
        for j in range(10):
            if (y+i > 119 or x+j > 159):
                return (False)
            if (r[y+i][x+j] < g[y+i][x+j] + 45 or r[y+i][x+j] < b[y+i][x+j] + 45):
                return (False)
    return (True)

while robot.go_on() :

    #Saves image
    colors = np.array(robot.get_camera())
    [r,g,b] = colors
    
    #Start by setting all color_on to False
    #Then iterate through the whole image with y and x coordinates
    #For every pixel, checks wether the pixel is considered red, blue or green. if Yes launch the check_color() function.
    #If the function returns true, then sets light to the detected color and sets color_on to True
    red_on = False
    green_on = False
    blue_on = False
    for y in range(119):
        for x in range(159):
            if (r[y][x] >= g[y][x] + 45 and r[y][x] >= b[y][x] + 45 and red_on == False):
                if (check_red(x, y, r, g, b)):
                    red_on = True
                    light_robot()
            elif (g[y][x] >= r[y][x] + 15 and g[y][x] >= b[y][y] + 15 and green_on == False):
                if (check_green(x, y, r, g, b)):
                    green_on = True
                    light_robot()
            elif (b[y][x] >= r[y][x] + 30 and b[y][x] >= g[y][x] + 30 and blue_on == False):
                if (check_blue(x, y, r, g, b)):
                    blue_on = True
                    light_robot()

    #If no block was detected, disable all lights
    if (red_on == False and blue_on == False and green_on == False):
        robot.disable_all_led()

robot.clean_up()

<table>
   <tr>
      <td><h1>Exploring robotics with <a href="https://www.epfl.ch/labs/mobots/robots-technologies/e-puck2">GCtronics E-Puck</a></h1>
The E-Puck was designed at the EPFL Autonomous Systems Lab and is open-hardware and its software open-source.
         <p/>
         <br>
      <b>🚩 <a href="https://github.com/oliolioli/Robotics/blob/main/Sensors.md">Sensor overview and analysis</a></b>
      </td><td><img src="https://github.com/oliolioli/Robotics/assets/4264535/20e8ebbf-b4f4-4f52-a3ea-d492a5e463fd" title="E-Puck robot, Image taken from https://e-puck.gctronic.com" alt="E-Puck robot, Image taken from https://e-puck.gctronic.com"></td>
   </tr>
</table>


<h2> ↪ Problems and solutions:</h2>
<b>
   
- [Braitenberg vehicles](#Braitenberg-vehicles)</b> - See [Braitenberg vehicle](https://en.wikipedia.org/wiki/Braitenberg_vehicle) for a short introduction.<b>
- [Line following](#Line-following)
- [Proportional–integral–derivative controller (PID) controlled behaviour](#PID-controlled-wand-following-behaviour)
- [Recognise coloured blocks](#Recognise-coloured-blocks)
- [Object recognition](#Object-recognition)
- [Communicate between robots with pooling messages](#Communicate-between-robots-with-pooling-messages)

 </b>
 </p>&nbsp;</p>
 

## Braitenberg vehicles ##

### Approaching obstacles ###

The following Braitenberg vehicle is designed to approach an obstacle it has spotted.

**Learnings:** The values proxL and proxR, and therefore also dsL and dsR, must increase with approaching an obstacle. This ultimately reduces the speed of the corresponding motors and allows to approach obstacles.

```python
proxR = ( a * prox_values [0] + b * prox_values [1] + c * prox_values [2] + d * prox_values [3]) / ( a + b + c + d )
proxL = ( a * prox_values [7] + b * prox_Object recognitionvalues [6] + c * prox_values [5] + d * prox_values [4]) / ( a + b + c + d )
dsR = ( NORM_SPEED * proxR ) / MAX_PROX
dsL = ( NORM_SPEED * proxL ) / MAX_PROX
speedR = ( NORM_SPEED - dsR )
speedL = ( NORM_SPEED - dsL )
```

### Exploring (avoiding instead of approaching obstacles) ###

The Braitenberg vehicle of the Explorer type should not approach an obstacle like the previous type, but rather avoid obstacles. This is achieved by the simple reversal of the
described above. If the sensor system recognises an obstacle, it is not approached but rather driven away from it. To do this, the motor control is simply reconfigured crosswise.

### Approaching obstacles, stop and explore further ###

The two vehicle types should now switch back and forth between their states.
To do this, it must be determined in a robust manner whether and when the approach is sufficiently balanced and the robot comes to a stop in front of the obstacle (behaviour is at equilibrium). It makes sense to model this behaviour as a finite state diagram.

The distance sensors can be used to determine the equilibrium in front of an obstacle. However, due to the signal noise, we have decided against this and determine the equilibrium using an average of the motor speed. We consider the speed adapted to the respective distance to be less fluctuating and therefore more robust for checking the equilibrium. To do this, we now continuously fill a list with the average value of the two motors during the journey. When the approaching robot approaches an obstacle, we compare the average speed of the last 30 saved values.

**💡 Learnings** 

Checking the equilibrium using the last 30 average speeds against a certain threshold value has proven to be very robust. Obstacles that are too low or too narrow are problematic, as they are difficult for the sensors to detect and therefore sometimes do not result in sufficient speed adjustment. Prioritising the front sensors so that narrower obstacles can also be detected might be an option here. For obstacles that are too low, on the other hand, the sensors
simply not designed for obstacles that are too low. Furthermore, the two rearmost sensors (3, 4) had to be given a negative weighting d of -2. This ensures that the robot actually moves away from the obstacle after changing state and does not approach the same obstacle again.

https://github.com/oliolioli/Robotics/assets/4264535/0f0dc9ea-8356-4ec1-b1bc-1f7502ccfeb0

_Video: Approaching obstacles, stop and explore further_

_💡 Unfortunately, due to the artificial lighting conditions, flickering was almost unavoidable in these and the following video recordings. 📹_


## Line following ##

Two sensors are positioned on a line and one remaining sensor on the white background. In this way, it can be recognised whether the robot is still following the line or deviating from it.

```python
elif ( gs [ MID ] > 500 and gs [ LEFT ] < 500) :
robot . set_speed (2 , 0)
elif ( gs [ LEFT ] > 500 and gs [ RIGHT ] < 500) :
robot . set_speed (0 , 2)
else :
robot . set_speed (2 , 2)
```

https://github.com/oliolioli/Robotics/assets/4264535/74a5d4dd-158e-4719-96a9-7b2cbbef6fd0

_Video: Following a line and do sharp turns_


**💡 Learnings** 

In order to follow the given line even on right-angled bends, a fast turn to the left or right must be initiated as soon as such a turn is reached.
must be initiated as soon as such a turn is reached. Such a sharp turn is tricky because all three sensors reach the same value at once, as they are all either on the line or have already left the bend. To deal with this, a counter counts 100 steps in each direction.

```python
elif ( gs [ MID ] < 500 and gs [ LEFT ] < 500 and gs [ RIGHT ] < 500) :
   state = " turn_left "
elif ( gs [ MID ] > 500 and gs [ LEFT ] > 500 and gs [ RIGHT ] > 500) :
   state = " turn_right "
```


## PID controlled wand following behaviour ##

In the following, an e-puck is to be optimised so that it follows the course of a wall using a [Proportional–integral–derivative controller (PID)](https://en.wikipedia.org/wiki/Proportional%E2%80%93integral%E2%80%93derivative_controller). A PID controller consists of three elements (P, I and D):
<b>
- P - Proportional (actual error)
- I - Integral (past error)
- D - derivative (approximation of future error)
</b>
PID controllers therefore represent a closed-loop control system, as past, current and even expected future errors are included in the calculation. The parameterisation of these parameters is not trivial: "simple to describe in principle, PID tuning is a difficult problem" [^1]. In the following, an attempt will be made to find ideal parameters so that the robot moves along the wall but does not touch it.

https://github.com/oliolioli/Robotics/assets/4264535/ec4084f7-43d5-42b0-987f-2caaa104e5f8

_Video: PID controlled block surrounding_


## Recognise coloured blocks ##

To do this, the entire image area (array of (160x120 pixels)) captured using robot.get camera() is iterated through.

```python
for y in range (119) :
   for x in range (159) :
      if ( r [ y ][ x ] >= g [ y ][ x ] + 45 and r [ y ][ x ] >= b [ y ][ x ] + 45 and red_on == False ) :
         if ( check_red (x , y , r , g , b ) ) :
            red_on = True
            light_robot ()
   elif ( g [ y ][ x ] >= r [ y ][ x ] + 15 and g [ y ][ x ] >= b [ y ][ y ] + 15 and green_on == False ) :
      if ( check_green (x , y , r , g , b ) ) :
         green_on = True
         light_robot ()
   elif ( b [ y ][ x ] >= r [ y ][ x ] + 30 and b [ y ][ x ] >= g [ y ][ x ] + 30 and blue_on == False ) :
      if ( check_blue (x , y , r , g , b ) ) :
         blue_on = True
         light_robot ()
```


As soon as one of the three colours is detected, the system checks whether a certain detected colour occurs from a certain position on a sufficient area. In this case, we can assume that a coloured block has been detected as such. Then the robot light up depending on which colors are detected.

https://github.com/oliolioli/Robotics/assets/4264535/6ef6fbd2-19ad-434a-bde5-63a94a192640

_Video: Recognising coloured blocks_


## Object recognition ##

The object recognition API recognises a wide variety of objects (see above). As the object recognition API not only provides the height and width but also the centre centre of the detected object in the X-axis and the Y-axis, we can determine the distance. After an initial calibration, we receive the object recognition information that corresponds to a desired distance of the target ten centimetres.

```python
# if distance ok, stay
if ((constMinHeight < meanH and meanH < constMaxHeight) or (constMinWidth < meanW and meanW < constMaxWidth)):
    print("Height and width ok - corrCommunicate between robots with pooling messagesect position")
    ds_backandforth = 0
# too far away, forward and love 
elif ((meanH < constMinHeight) and (meanW < constMinWidth)):
    print("Forward")
    ds_backandforth = 1
# too near, go back    
else:
    print("Backward")
    ds_backandforth = -0.8
```

The backward movement is deliberately chosen to be smaller, as the object has already been found. Therefore we no longer need to find an object, but rather only have to drive a little further backwards in order to move away from the object. Within a certain tolerance range, the robot finally stops and no longer moves.

```python
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
    ds_left = 0Communicate between robots
    ds_right = 0
```

Now the values of the forward and backward movement ds_backandforth and any left or right rotation ds_left and ds_right are added to the left and right motor speeds. In this way, the robot moves towards or away from a more distant obstacle.

https://github.com/oliolioli/Robotics/assets/4264535/bafca50c-4494-42a7-b0a7-4fb7abd72ce9

_Video: Object recognition_


**💡 Learnings** 
Finding an ideal tolerance range at which the robot would ultimately come to a standstill was the  the most difficult part of this implementation. The sensors provide such volatile data that the robot tended to correct far too quickly and too much. The use of average values using an array was useful for smoothing this data.
Finally, a sufficiently large tolerance also had to be selected so that the robot could doesn't correct its position due to sensor outliers.

## Communicate between robots with pooling messages ##

With the communication module, which is loaded with the init client **communication() function**, the e-pucks communicate pucks do not communicate directly with each other via a communication server, but they can send messages to a shared server with **send_msg()** and receive messages from this server with **robot.receive msg()**.

With established communication, robots can synchronise their sensor data and thus check whether they are in the same environment, for example. The coloured blocks can be easily recognised and categorised using the object recognition API discussed above categorised and matched with other robots.

If the corresponding bit is set to one, otherwise it remains at zero. This gives us a simple code that reflects the blocks recognised by the robot in its environment. For example, a single red block would be displayed with the code 100, a green block with a blue block with 011. Messages are only sent if coloured blocks are actually detected. This keeps the message volume as small as possible and makes it easier to interpret, as the recognised environment must be compared with the environment recognised by the neighbouring e-puck. If the robot now receives the same message as it sends, it sees the same objects in its environment. If both robots recognise the same configuration, all their LEDs are activated.

https://github.com/oliolioli/Robotics/assets/4264535/69c0293e-a9a2-4aa4-ab53-90c3b8b32392

_Video: Inter-robot communication through message pooling_


[^1]: https://en.wikipedia.org/wiki/PID_controller

# Robotics #
Exploring robotics with [GCtronics E-Puck](https://www.epfl.ch/labs/mobots/robots-technologies/e-puck2).
The E-Puck was designed at the EPFL Autonomous Systems Lab and is open-hardware and its software open-source.

<table>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/20e8ebbf-b4f4-4f52-a3ea-d492a5e463fd" alt="E-Puck robot, Image taken from https://e-puck.gctronic.com" width="50%" height="50%">
</td><td><b>🚩 <a href="https://github.com/oliolioli/Robotics/blob/main/Sensors.md">Sensor overview and anaylsis</a></b></td>
  </tr>
</table>


- [Braitenberg vehicles](#Braitenberg-vehicles)
- [Line following](#Line-following)
- [Wand following behaviour (PID: proportional-integral-derivative controller)](#Wand-following-behaviour-(PID))


## Braitenberg vehicles ##

See [Braitenberg vehicle](https://en.wikipedia.org/wiki/Braitenberg_vehicle) for a short introduction.

### Approaching obstacles ###

The following Braitenberg vehicle is designed to approach an obstacle it has spotted.

**Learnings:** The values proxL and proxR, and therefore also dsL and dsR, must increase with approaching an obstacle. This ultimately reduces the speed of the corresponding motors and allows to approach obstacles.

```python
proxR = ( a * prox_values [0] + b * prox_values [1] + c * prox_values [2] + d * prox_values [3]) / ( a + b + c + d )
proxL = ( a * prox_values [7] + b * prox_values [6] + c * prox_values [5] + d * prox_values [4]) / ( a + b + c + d )
dsR = ( NORM_SPEED * proxR ) / MAX_PROX
dsL = ( NORM_SPEED * proxL ) / MAX_PROX
speedR = ( NORM_SPEED - dsR )
speedL = ( NORM_SPEED - dsL )
```

💡 Unfortunately, due to the artificial lighting conditions, flickering was almost unavoidable in these and the following video recordings. 📹

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


### Line following ###

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


### Wand following behaviour (PID) ###

In the following, an e-puck is to be optimised so that it follows the course of a wall using a [PID controller](https://en.wikipedia.org/wiki/Proportional%E2%80%93integral%E2%80%93derivative_controller) . A PID controller consists of three elements (P, I and D):
- P - Proportional (actual error)
- I - Integral (past error)
- D - derivative (approximation of future error)

PID controllers therefore represent a closed-loop control system, as past, current and even expected future errors are included in the calculation. The parameterisation of these parameters is not trivial: "simple to describe in principle, PID tuning is a difficult problem"[^1]. In the following, an attempt will be made to find ideal parameters so that the robot moves along the wall but does not touch it.

https://github.com/oliolioli/Robotics/assets/4264535/ec4084f7-43d5-42b0-987f-2caaa104e5f8

_Video: PID controlled block surrounding_



[^1]: https://en.wikipedia.org/wiki/PID_controller

# E-Puck Sensors #

The following is a detailed analysis of the sensors
- infrared distance sensor
- infrared floor sensors
- camera, microphones
- object recognition via programming interface

## Proximity infra-red sensors ##

We initialise the robot's sensors and calibrate the infrared sensors. We plot the calibration data. For now, we are only interested in the proximity infrared sensors (PROX RIGHT FRONT and PROX LEFT FRONT) of the robot front. The relevant information can be found in the GCTronic specification[^1]

![image](https://github.com/oliolioli/Robotics/assets/4264535/60756dc9-6ed8-4cfa-9c25-9c1cd0529279)

We output the two constants PROX LEFT FRONT and PROX RIGHT FRONT using a print command and determine that the numbering of the sensors (7, 0) matches the specification. The generated plot shows the values of the above-mentioned left and right infrared sensors on the Y-axis. The X-axis (steps) indicates the number of steps the robot has taken away from the obstacle at the time of the measurement. We recognise the decreasing values of the infrared sensors with increasing number of steps and thus greater distance.

![image](https://github.com/oliolioli/Robotics/assets/4264535/403a406f-dc51-4b47-b276-d04d071d8089)

### Ground sensors ###

![image](https://github.com/oliolioli/Robotics/assets/4264535/01f7d0ac-3de5-4c95-a83d-44bbb603cf02)

![image](https://github.com/oliolioli/Robotics/assets/4264535/2fbc87e7-bad2-4672-a514-2d734a0221df)



[^1]: [Wiki GCtronic e-puck2](https://www.gctronic.com/doc/index.php?title=e-puck2)

# E-Puck Sensors #

The following is a detailed analysis of the following sensors
- infrared distance sensor
- infrared floor sensors
- camera, microphones
- object recognition via programming interface

## Proximity infra-red sensors ##

We initialise the robot's sensors and calibrate the infrared sensors. We plot the calibration data. For now, we are only interested in the proximity infrared sensors (PROX RIGHT FRONT and PROX LEFT FRONT) of the robot front. The relevant information can be found in the GCTronic specification[^1]

<table>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/60756dc9-6ed8-4cfa-9c25-9c1cd0529279" alt=""></td><td><img src="https://github.com/oliolioli/Robotics/assets/4264535/403a406f-dc51-4b47-b276-d04d071d8089" alt=""></td>
  </tr>
</table>

We output the two constants PROX LEFT FRONT and PROX RIGHT FRONT using a print command and determine that the numbering of the sensors (7, 0) matches the specification. The generated plot shows the values of the above-mentioned left and right infrared sensors on the Y-axis. The X-axis (steps) indicates the number of steps the robot has taken away from the obstacle at the time of the measurement. We recognise the decreasing values of the infrared sensors with increasing number of steps and thus greater distance.

The noise of the sensors is clearly recognisable: The noise is particularly visible with the strongly fluctuating values in the range between 20 and 50 steps and also strongly differing values between the left and right sensors.

## Infrared floor sensors ##

There are three infrared floor sensors in the lower section at the front of the E-Puck.

<table>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/01f7d0ac-3de5-4c95-a83d-44bbb603cf02" alt=""></td><td><img src="https://github.com/oliolioli/Robotics/assets/4264535/2fbc87e7-bad2-4672-a514-2d734a0221df" alt=""></td><td><img src="https://github.com/oliolioli/Robotics/assets/4264535/bcce3666-e59a-404d-ac44-715f7c9af859 alt="Colored lines for ground sensor testing"></td>
  </tr>
</table>

We use the **robot.init ground()** function to test the response behaviour of the sensors. The value range of these sensors should vary between 1000 (pure white) and 0 (black).
fluctuate. A white sheet with coloured lines glued to it will serve as our test setup: 
We place the robot on the bottom white edge of the paper and then let it vertically over all the lines. The generated plots clearly show that the two black lines (first and fourth line) lead to impressive deflections of the sensors. Although the plotted curve also shows clearly visible deflections in the traverse of the remaining coloured lines, these are only between 1000 and 900 and are therefore very close to the values for pure white. To control a robot with floor markings, the clear black colour is therefore very suitable.


We can clearly see the different sensitivity of the three individual floor sensors. 
If we let the robot move diagonally across the sheet with the coloured lines at an approximate angle of 45° - from bottom left to top right in the middle - our measured values shift on the X-axis (step). This is because the three floor sensors on the front of the robot are all on the same horizontal line. Therefore, the above-mentioned shift in the respective sensor deflections occurs when the lines are crossed.

[^1]: [Wiki GCtronic e-puck2](https://www.gctronic.com/doc/index.php?title=e-puck2)

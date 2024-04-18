# E-Puck Sensors #

The following is a detailed analysis of the following sensors
- infrared distance sensor
- infrared floor sensors
- camera, microphones
- object recognition via programming interface

## Proximity infra-red sensors ##

We initialise the robot's sensors and calibrate the infrared sensors. We plot the calibration data. For now, we are only interested in the proximity infrared sensors (**PROX LEFT FRONT** and **PROX RIGHT FRONT** ) of the robot front. The relevant information can be found in the GCTronic specification[^1]

<table>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/60756dc9-6ed8-4cfa-9c25-9c1cd0529279" alt=""></td><td><img src="https://github.com/oliolioli/Robotics/assets/4264535/403a406f-dc51-4b47-b276-d04d071d8089" alt=""></td>
  </tr>
</table>

The generated plot shows the values of the above-mentioned left and right infrared sensors on the Y-axis. The X-axis (steps) indicates the number of steps the robot has taken away from the obstacle at the time of the measurement. We recognise the decreasing values of the infrared sensors with increasing number of steps and thus greater distance.

The noise of the sensors is clearly recognisable: The noise is particularly visible with the strongly fluctuating values in the range between 20 and 50 steps and also strongly differing values between the left and right sensors.

## Infrared floor sensors ##

There are three infrared floor sensors in the lower section at the front of the E-Puck.

<table>
  <th>Floor sensors front and bottom view</th><th>Colored lines for ground sensor testing</th>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/01f7d0ac-3de5-4c95-a83d-44bbb603cf02" alt="Floor sensors front view">
      <img src="https://github.com/oliolioli/Robotics/assets/4264535/2fbc87e7-bad2-4672-a514-2d734a0221df" alt="Floor sensors bottom view"></td>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/bcce3666-e59a-404d-ac44-715f7c9af859 alt="Colored lines for ground sensor testing"></td>
  </tr>
</table>

We use the **robot.init ground()** function to test the response behaviour of the sensors. The value range of these sensors should **vary between 1000 (pure white) and 0 (black)**. A white sheet with coloured lines glued to it will serve as our test setup: 
We place the robot on the bottom white edge of the paper and then let it vertically over all the lines. 

<table>
  <th colspan="2">move diagonally across the sheet with the coloured lines at an approximate angle of 45°</th>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/5002bd56-23a8-4fdd-aabe-a7f4ae6ee316"></td>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/a938e8e6-57ef-4455-aad4-de09f2cc36d3"></td>
  </tr>
</table>

The generated plots clearly show that the two black lines (first and fourth line) lead to impressive deflections of the sensors. Although the plotted curve also shows clearly visible deflections in the traverse of the remaining coloured lines, these are only between 1000 and 900 and are therefore very close to the values for pure white. To control a robot with floor markings, the clear black colour is therefore very suitable.

## Camera & microphones ##

### Initialising the camera ##
![image](https://github.com/oliolioli/Robotics/assets/4264535/f2f824b9-fce5-4a8a-8e58-3d4199ba4824)
Historam in front of red block

## object recognition via programming interface ##

[^1]: [Wiki GCtronic e-puck2](https://www.gctronic.com/doc/index.php?title=e-puck2)

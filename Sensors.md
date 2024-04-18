# E-Puck Sensors #

The following is a detailed analysis of the following sensors
- [Proximity infra-red sensors](#infrared-distance-sensor)
- [Infrared floor sensors](#infrared-floor-sensors)
- [Camera and microphones](#Camera-and-microphones)
- [Object recognition via programming interface](#Object-recognition-via-programming-interface)

## Proximity infra-red sensors ##

We initialise the robot's sensors and calibrate the infrared sensors. We plot the calibration data. For now, we are only interested in the proximity infrared sensors (**PROX LEFT FRONT** and **PROX RIGHT FRONT** ) of the robot front. The relevant information can be found in the GCTronic specification[^1]

<table>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/60756dc9-6ed8-4cfa-9c25-9c1cd0529279" alt="" height="90%" width="90%"></td>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/403a406f-dc51-4b47-b276-d04d071d8089" alt="" height="90%" width="90%"></td>
  </tr>
  <tr><td colspan="2"><i>The generated plot shows the values of the above-mentioned left and right infrared sensors on the Y-axis. The X-axis (steps) indicates the number of steps the robot has taken away from the obstacle at the time of the measurement. We recognise the decreasing values of the infrared sensors with increasing number of steps and thus greater distance.

The noise of the sensors is clearly recognisable: The noise is particularly visible with the strongly fluctuating values in the range between 20 and 50 steps and also strongly differing values between the left and right sensors.
</i></tr>
</table>


## Infrared floor sensors ##

There are three infrared floor sensors in the lower section at the front of the E-Puck. We use the **robot.init ground()** function to test the response behaviour of the sensors.

<table>
  <th>Floor sensors front view</th><th>Floor sensors bottom view</th><th>Colored lines for ground sensor testing</th>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/01f7d0ac-3de5-4c95-a83d-44bbb603cf02" alt="Floor sensors front view" height="90%" width="90%">
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/2fbc87e7-bad2-4672-a514-2d734a0221df" alt="Floor sensors bottom view height="90%" width="90%""></td>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/bcce3666-e59a-404d-ac44-715f7c9af859 alt="Colored lines for ground sensor testing" height="70%" width="70%"></td>
  </tr>
</table>

The value range of these sensors should **vary between 1000 (pure white) and 0 (black)**. A white sheet with coloured lines glued to it will serve as our test setup: 
We place the robot on the bottom white edge of the paper and then let it vertically over all the lines. 

<table>
  <th colspan="2">move diagonally across the sheet with the coloured lines at an approximate angle of 45°</th>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/5002bd56-23a8-4fdd-aabe-a7f4ae6ee316" height="70%" width="70%"></td>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/a938e8e6-57ef-4455-aad4-de09f2cc36d3" height="70%" width="70%"></td>
    <tr><td colspan="2"><i>The generated plots clearly show that the two black lines (first and fourth line) lead to impressive deflections of the sensors. Although the plotted curve also shows clearly visible deflections in the traverse of the remaining coloured lines, these are only between 1000 and 900 and are therefore very close to the values for pure white. To control a robot with floor markings, the clear black colour is therefore very suitable.</i></td></tr>
  </tr>
</table>

## Camera and microphones ##

### Initialising camera and microphones##

<table>
  <th>Histogram in front of red block (without letterboxing)</th><th>Test of the microphones during pass-by</th>
  <tr><td><img src="https://github.com/oliolioli/Robotics/assets/4264535/f2f824b9-fce5-4a8a-8e58-3d4199ba4824" height="50%" width="50%"></td><td><img src="https://github.com/oliolioli/Robotics/assets/4264535/2e56b042-a98d-4557-8f3a-a6d97d49c9fa"></td>
  </tr>
  <tr><td colspan="2"><i>The colour recognition delivers extremely different results, red is best recognised.
The microphones have different sensitivities, particularly with regard to their different orientation and position.</i></tr>
</table>


## Object recognition via programming interface ##

We let the robot scan an environment of different coloured blocks at different distances, a black ball and another e-puck. The robot rotates around itself, saves the resulting images and creates a CSV document with 350 measurements (approximately two measurements per step). The resulting measurements contain the following information: _x_centre, y_centre, width, height, conf and label_, where x- and y_centre describe the detected centres of the respective objects.

In addition to the self-explanatory width and height attributes, **conf and label** are of particular interest. The label assumes the values red block, green block, blue block or black block, but can also recognise black ball or epuck.

<table>
  <th colspan="2">Recognition of a blue and yellow blocks</th>
  <tr>
    <td rowspan="2"></td><img src="https://github.com/oliolioli/Robotics/assets/4264535/4be117b2-b99e-454e-a871-61131cf616cf" alt="E-Puck Object recognition" height="70%" width="70%"><br/>
<i>The treshold (here: 0.7) is crucial for object recognition and must be determined heuristically.</i>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/8eb0aeaa-83b5-4055-a502-221718beca1e" alt="Recognition of a blue block" height="110%" width="110%"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/d36ae43b-3065-42da-90a5-01f94eed910a" alt="Recognition of a blue and yellow block" height="110%" width="110%"></td>
  </tr>
</table>



<table>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/8eb0aeaa-83b5-4055-a502-221718beca1e" alt="Recognition of a blue block" height="110%" width="110%"></td><td><img src="https://github.com/oliolioli/Robotics/assets/4264535/d36ae43b-3065-42da-90a5-01f94eed910a" alt="Recognition of a blue and yellow block"></td>
  </tr>
</table>

[^1]: [Wiki GCtronic e-puck2](https://www.gctronic.com/doc/index.php?title=e-puck2)

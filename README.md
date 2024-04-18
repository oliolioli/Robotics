# Robotics #
Exploring robotics with [GCtronics E-Puck](https://www.epfl.ch/labs/mobots/robots-technologies/e-puck2).
The E-Puck was designed at the EPFL Autonomous Systems Lab and is open-hardware and its software open-source.

<table>
  <tr>
    <td><img src="https://github.com/oliolioli/Robotics/assets/4264535/20e8ebbf-b4f4-4f52-a3ea-d492a5e463fd" alt="E-Puck robot, Image taken from https://e-puck.gctronic.com" width="50%" height="50%">
</td><td><b>🚩 <a href="https://github.com/oliolioli/Robotics/blob/main/Sensors.md">Sensor overview and anaylsis</a></b></td>
  </tr>
</table>


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




https://github.com/oliolioli/Robotics/assets/4264535/0f0dc9ea-8356-4ec1-b1bc-1f7502ccfeb0

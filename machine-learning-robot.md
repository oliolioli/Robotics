# Machine learning to recognize distance and angle of an audio signal #

## Problem description ##

The challenge was for the e-puck to learn and recognise the angle and distance to an incoming, predefined audio signal in a given environment using machine learning[8]. As soon as the predefined sound is played at a random location in the predefined setup environment, the e-puck should move towards the sound source.

## Solution strategy ##

To solve this problem, the basic consideration is that the four audio sensors of the e-puck (see Figure 4.16 and specification[3]) must necessarily receive an audio signal at different levels and at different times. Audio signals played at a certain angle to the side of the e-puck can also be recognised in principle by their pattern. Figures 4.22, 4.23 and 4.24, for example, clearly show the extent to which
a lateral signal leaves its own signature on the four audio sensors. For these reasons, the e-puck can in principle be taught from which angle and from which distance an audio signal is sent using machine learning. As a solution strategy, this problem can be divided into various sub-problems:

1. testing the audio sensors and determining a setup,
2. generating as many qualitative data sets as possible and extracting them,
3. training and testing the model

## Implementation ##
### Checking the setup and audio sensors ###
The first test of the four audio sensors revealed that the API supplied did not allow sufficient difference to be detected in the four different inputs to be able to generate different data sets per sensor at all. For this reason, the decision was made to add additional 'ears' to the four audio sensors of the e-puck using 3D printing, which can be placed on the e-puck and include the four audio sensors. 

Partition walls are fitted between these individual 'ears', which are additionally insulated with additional filling material. In figure ... (without ears) and Figure ... (with ears) the improvement is clear: the individual audio tracks are much further apart and there is hardly any overlap. Noise interference has also been minimised: the four audio tracks can be distinguished much more clearly, making their so-called features more distinct and facilitating machine learning.

A simple beep was selected as the audio signal. The following setup was selected to generate the actual data sets: The e-puck stands statically in the centre of three circles with a radius of sixteen, 32 and 48cm. These three circles are divided into sectors of eighteen degrees, resulting in twenty different sectors per circle (20*18°=360°). These circles and the division into sectors are drawn on a large sheet of paper and guarantee a constant environment. While the e-puck is placed statically in the centre, a constant sound (in all directions) is emitted at the respective points of the circles using an audio device.

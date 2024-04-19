# Machine learning to recognize distance and angle of an audio signal #

## Problem description ##

The challenge was for the e-puck to learn and recognise the angle and distance to an incoming, predefined audio signal in a given environment using machine learning[8]. As soon as the predefined sound is played at a random location in the predefined setup environment, the e-puck should move towards the sound source.

## Solution strategy ##

To solve this problem, the basic consideration is that the four audio sensors of the e-puck (see Figure 4.16 and specification[3]) must necessarily receive an audio signal at different levels and at different times. Audio signals played at a certain angle to the side of the e-puck can also be recognised in principle by their pattern. Figures 4.22, 4.23 and 4.24, for example, clearly show the extent to which
a lateral signal leaves its own signature on the four audio sensors. For these reasons, the e-puck can in principle be taught from which angle and from which distance an audio signal is sent using machine learning. As a solution strategy, this problem can be divided into various sub-problems:

1. testing the audio sensors and determining a setup,
2. generating as many qualitative data sets as possible and extracting them,
3. training and testing the model

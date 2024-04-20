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

### Generation and extraction of data records ###
The above setup leads to twenty points on each distance circle and thus to a total of 60 different measuring points. A beep is now automatically played at each of these measuring points using the record.py script and the inputs of all four audio sensors are recorded. These recordings are made manually for each specific distance and angle and create a CSV file with the following name **file<counter>_D<32>_A<18>.csv** for each point of the setup, whereby in this example a circle radius of 32cm and an angle of 18° are encoded in the file name. For each measuring point, 60 such CSV files are created by the **sound_extractor.py** script. With the total of 60 points (**three radii with 20 points each**) of the setup, this **results in a total of 3600 data records.**

The **sound_extractor.py** script then **extracts the individual tracks of the audio sensors from the stored data records**. The maximum and average volume of the beep are extracted from these. As four audio sensors with an average value and a maximum value are stored for each beep, eight so-called features can be extracted per data set. In this script, the main() function simply writes the angle or distance of the respective data set and the eight features to one line, which are then merged and written to two large files: angle_all.csv and distance_all.csv, which will ultimately lead to two different models. In the end, both files contain around 3600 data records, but certain individual entries have to be removed due to noise, for example.


### Training and testing the model ###
Now the software SciKit[11] is used, which can be used to create so-called random forests[9][10]. Using the ia.py script, both angle_all.csv and distance_all.csv files are now processed individually by hand. First, the data is sorted randomly. Then 80% of the data is used to train the so-called RandomForest (train). The remaining 20% is used for later validation (test).

The first line of each data set and the last eight lines of each data set (with the 2*4 features) are now written to variables y_train and x_train. These two variables are now transferred to the generated decision tree using the fit() function. The decision tree thus receives the information about the angle or distance and the corresponding eight features. With this information, the various models can now be generated and the most promising can finally be selected for classification tasks[9]. This work is done for us by the Python library SciKit[11].

## Validation ##

### Automatic validation ###
The two models created, Random_forest_model_distance.pkl and Random_forest_model_angle.pkl, can now also be validated using the ia.py script, which checks tests against predictions and outputs the corresponding error.
With the RandomForest created by SciKit, we consistently obtain very satisfactory results. In Table 3.1 below, we can see that the e-puck only misjudges a played sound that is sixteen centimetres away in five out of a hundred cases. And this misjudgement is only 18°. Although the error rate increases with increasing distance, remarkably it is completely wrong in very few cases
and in most cases only by 18°.



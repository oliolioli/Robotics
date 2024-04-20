# run the script to plot the additional sensor responses 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# select data to plot
columns = [
    'Angle',
    'mic0',
    'mic1',
    'mic2',
    'mic3',
    #'placeholder' # here for ease of commenting in/out
     ]

# get data from CSV file
csv = pd.read_csv('maxVolume.csv', index_col=0)

# drop last empty column
csv.drop(csv.columns[-1], axis=1, inplace = True)

# select columns to plot (removing placeholder)
new_csv = csv[columns[:-1]]
csv = new_csv

# plot single sensor one by one with subplots
csv.plot(subplots=True,sharey='col')
# save plot
plt.savefig('additional_sensors_single.png')
plt.show()

# plot all sensors on single plot
csv.plot()
# set the legend on right corner
plt.legend(loc='upper right')
plt.savefig('additional_sensors.png')
plt.show() 

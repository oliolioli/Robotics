import pickle
from unifr_api_epuck import wrapper
from playsound import playsound
import numpy as np
import csv

MY_IP = '192.168.2.108'
MAX_STEPS = 200
audio = [[]]
inverted = False

robot = wrapper.get_robot(MY_IP)

STARTING_STEPS = robot.get_motors_steps()[0]

def get_actual_steps():
	return (abs(robot.get_motors_steps()[0] - STARTING_STEPS))

def get_mic(data, nbr):
	done = False
	sound = []

	for input_value in data:
		value = int(input_value[nbr])
		if (value >= 20 and not done):
			sound.append(value)
		if (value < 20 and len(sound) >= 20):
			done = True
		elif (len(sound) < 20 and not done and value < 20):
			sound = []
	return (sound)

def parse_file(data):
	sounds = [[]] * 4
	values = np.zeros((2, 4))
	for i in range(4):
		sounds[i] = get_mic(data, i)
		values[0][i] = max(sounds[i])
		values[1][i] = sum(sounds[i]) / len(sounds[i])
	return (values)

with open('Random_forest_model_distance.pkl', 'rb') as file_dist:
	model_dist = pickle.load(file_dist)

with open('Random_forest_model_angle.pkl', 'rb') as file_angle:
	model_angle = pickle.load(file_angle)

for step in range(MAX_STEPS):
	if (step == 20):
		playsound('1s_beep.mp3')
	audio.append(robot.get_microphones())
	robot.go_on()

audio = audio[1:]						# erste Zeile entfernen
values = parse_file(audio)				# wie in SoundExtractor - Features auslesen
values = values.flatten()				# flatten
values = values.reshape(1, -1)			# reshape

angle = model_angle.predict(values)
dist = model_dist.predict(values)

print(angle)
print(dist)

if (int(angle) > 180):
	angle = 360 - int(angle)
	inverted = True
else:
	angle = int(angle)
	inverted = False

while (robot.go_on() and get_actual_steps() < angle / 18 * 62):			# nur noch angepasst Anzahl Schritte machen (in die richtige Richtung)
	if (inverted):
		robot.set_speed(-0.5, 0.5)
	else:
		robot.set_speed(0.5, -0.5)

robot.set_speed(0, 0)
STARTING_STEPS = robot.get_motors_steps()[0]							# Steps müssen reseted werden

while (robot.go_on() and get_actual_steps() < int(dist) / 16 * 1150):
	robot.set_speed(2, 2)

robot.clean_up()

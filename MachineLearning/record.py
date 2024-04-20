# run the script to generate additional sensor data 
from unifr_api_epuck import wrapper
from playsound import playsound
import time

MY_IP = '192.168.2.108'
MAX_STEPS = 200
counter = 0

robot = wrapper.get_robot(MY_IP)

while counter < 31:
	filename = "file" + str(counter) + "_D32_A18.csv"
	data = open(filename, "w")

	if data == None:
		print('Error opening data file!\n')
		quit

	#write header in CSV file
	data.write('step,')
	data.write('mic0,mic1,mic2,mic3,')
	data.write('\n')
	for step in range(MAX_STEPS):
		if (step == 20):
			playsound('1s_beep.mp3')
		#write a line of data 
		data.write(str(step)+',')
		mic = robot.get_microphones()
		robot.go_on()
		for v in mic:
			data.write(str(v)+',')

		data.write('\n')
	counter += 1
	
	data.close()

robot.clean_up()

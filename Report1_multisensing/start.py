from subprocess import call
import time
import os
import datetime as df


difference = 5

while True :
	
	detect_time = df.datetime.now() - df.timedelta(seconds = difference)
	detect = detect_time.strftime('%Y-%m-%d_%H:%M:%S')


	
	if os.path.isfile("/home/seloco2/nfs/{}.jpg" .format(detect)) :
		call(['/home/seloco2/darknet/darknet', 'detect', 'cfg/yolov3.cfg', 'yolov3.weights', '/home/seloco2/nfs/{}.jpg'.format(detect)])
		difference = (df.datetime.now() - detect_time).seconds -1

	else :
		print("waiting for image file...\r", end='')
		if difference > 5 :
			difference = difference - 1
	


	

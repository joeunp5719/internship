from picamera import PiCamera
from time import sleep
from subprocess import call
import RPi.GPIO as gpio
import time
import datetime as dt


gpio.setmode(gpio.BCM)

#cho-eum-pa
pin_trig = 3
pin_echo = 2
gpio.setup(pin_trig, gpio.OUT)
gpio.setup(pin_echo, gpio.IN)

#move
pin_move = 4
gpio.setup(pin_move, gpio.IN)


#camera
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.framerate = 15



def sensor_cho() :
    gpio.output(pin_trig, False)
    time.sleep(0.5)
    gpio.output(pin_trig, True)
    time.sleep(0.00001)
    gpio.output(pin_trig, False)


    while gpio.input(pin_echo) == 0 :
        pulse_start = time.time()

    while gpio.input(pin_echo) == 1 :
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)

    print("Distance : ", distance, "cm")

    return distance


def sensor_move() :
    ismove = 0

    if gpio.input(pin_move) is gpio.HIGH :
        time.sleep(1)
        if gpio.input(pin_move) is gpio.HIGH :
            ismove = 1

    return ismove




while True :
    if sensor_cho() < 100 :
        if sensor_move() == 1 :
            current = dt.datetime.now()
            current_time = current.strftime('%Y-%m-%d_%H:%M:%S')
            camera.capture('/home/pi/Documents/nfs/{}.jpg'.format(current_time))
            print("captured")
    sleep(1)

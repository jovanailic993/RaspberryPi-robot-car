from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print"Type: direction(rotations, speed)"
pins = [4,17,27,22,26,19,13,6]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)


def anticlockwiseleft(rotations, speed):
    sleep_time=0.1 / float(speed)
    for loop in range(1,int(512*float(rotations))):
        GPIO.output(4,1)
        sleep(sleep_time)
        GPIO.output(22,0)
        sleep(sleep_time)
        GPIO.output(17,1)
        sleep(sleep_time)
        GPIO.output(4,0)
        sleep(sleep_time)
        GPIO.output(27,1)
        sleep(sleep_time)
        GPIO.output(17,0)
        sleep(sleep_time)
        GPIO.output(22,1)
        sleep(sleep_time)
        GPIO.output(27,0)
        sleep(sleep_time)
    GPIO.output(22,0)

def clockwiseleft(rotations, speed):
    sleep_time=0.1 / float(speed)
    for loop in range(1,int(512*float(rotations))):
        GPIO.output(22,1)
        sleep(sleep_time)
        GPIO.output(4,0)
        sleep(sleep_time)
        GPIO.output(27,1)
        sleep(sleep_time)
        GPIO.output(22,0)
        sleep(sleep_time)
        GPIO.output(17,1)
        sleep(sleep_time)
        GPIO.output(27,0)
        sleep(sleep_time)
        GPIO.output(4,1)
        sleep(sleep_time)
        GPIO.output(17,0)
        sleep(sleep_time)
    GPIO.output(4,0)

def anticlockwiseright(rotations, speed):
    sleep_time=0.1 / float(speed)
    for loop in range(1,int(512*float(rotations))):
        GPIO.output(26,1)
        sleep(sleep_time)
        GPIO.output(6,0)
        sleep(sleep_time)
        GPIO.output(19,1)
        sleep(sleep_time)
        GPIO.output(26,0)
        sleep(sleep_time)
        GPIO.output(13,1)
        sleep(sleep_time)
        GPIO.output(19,0)
        sleep(sleep_time)
        GPIO.output(6,1)
        sleep(sleep_time)
        GPIO.output(13,0)
        sleep(sleep_time)
    GPIO.output(6,0)

def clockwiseright(rotations, speed):
    sleep_time=0.1 / float(speed)
    for loop in range(1,int(512*float(rotations))):
        GPIO.output(6,1)
        sleep(sleep_time)
        GPIO.output(26,0)
        sleep(sleep_time)
        GPIO.output(13,1)
        sleep(sleep_time)
        GPIO.output(6,0)
        sleep(sleep_time)
        GPIO.output(19,1)
        sleep(sleep_time)
        GPIO.output(13,0)
        sleep(sleep_time)
        GPIO.output(26,1)
        sleep(sleep_time)
        GPIO.output(19,0)
        sleep(sleep_time)
    GPIO.output(26,0)
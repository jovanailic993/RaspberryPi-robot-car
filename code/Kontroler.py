import os
import sys
import threading
import time
import RPi.GPIO as GPIO
import time
import stepmotor
import testServo
import web

stanje=True

class NitSve(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		global stanje
		stanje= True		
		while(stanje):
			mineServo = testServo.myServo()
			t3 = Scanner()
			t3.start()
			while not t3.shortDistance:
				move_forward(rotations=0.3)
				if(not stanje):
					return
			rotate_left()
			t3.shortDistance = False
			t3.join()    

	def zaustavi(self):
		global stanje
		stanje=False
		GPIO.cleanup()


GPIO.setmode(GPIO.BCM)
TRIG = 12 
ECHO = 5
GPIO.setwarnings(False)
print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def scan():
	GPIO.output(TRIG, False)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	distance = round((pulse_end-pulse_start) * 17000,2)
	return distance
	GPIO.cleanup()



class FrontLeft(threading.Thread):
	def __init__(self, rotations=0.9):
		threading.Thread.__init__(self)
		self.rotations = rotations

	def run(self):
		print "run left"
		stepmotor.anticlockwiseleft(self.rotations, 70)


class FrontRight(threading.Thread):
	def __init__(self, rotations=0.9):
		threading.Thread.__init__(self)
		self.rotations = rotations

	def run(self):
		print "run right"
		stepmotor.anticlockwiseright(self.rotations, 70)


class BackLeft(threading.Thread):
	def __init__(self, rotations=0.9):
		threading.Thread.__init__(self)
		self.rotations = rotations

	def run(self):
		print "run left"
		stepmotor.clockwiseleft(self.rotations, 70)


class BackRight(threading.Thread):
	def __init__(self, rotations=0.9):
		threading.Thread.__init__(self)
		self.rotations = rotations
	def run(self):
		print "run right"
		stepmotor.clockwiseright(self.rotations, 70)




class Scanner(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.shortDistance = False
	
		
	def run(self):
		while True:
			print "scanning"
			
			distance = scan()
			time.sleep(0.2)
			print "Distance is %d cm" % distance
			if distance < 30:
				self.shortDistance = True
				return




def move_forward(rotations=0.9):
	
	t1 = FrontLeft(rotations)
	t2 = FrontRight(rotations)
	t1.start()
	t2.start()
	t1.join()
	t2.join()


def move_backward(rotations=0.9):

	t1 = BackLeft(rotations)
	t2 = BackRight(rotations)
	t1.start()
	t2.start()
	t1.join()
	t2.join()


def rotate_left(rotations=0.9):

	t1 = FrontRight(rotations)
	t2 = BackLeft(rotations)
	t1.start()
	t2.start()
	t1.join()
	t2.join()


def rotate_right(rotations=0.9):

	t1 = FrontLeft(rotations)
	t2 = BackRight(rotations)
	t1.start()
	t2.start()
	t1.join()
	t2.join()

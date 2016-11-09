import RPi.GPIO as GPIO
import time
import requests
import json
import urllib2


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 12 
ECHO = 5

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


print "Waiting For Sensor To Settle"
while True:
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.output(TRIG, False)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	distance = round((pulse_end-pulse_start) * 17000,2)
	print distance
	
	GPIO.cleanup()
	
	
	data = {}
	data["senzorID"]=3
	data["vrednost"]=distance
	req = urllib2.Request("http://172.20.221.217/iot/api/dodajVrednost/", data=json.dumps(data),
	                      headers={"Content-Type": "application/json", "X-ELAB-IOT-Kljuc": "D8CB95892FD486EDFE356A9CFB4A52FD2980CE42"})
	print urllib2.urlopen(req).read()
	
	time.sleep(3)
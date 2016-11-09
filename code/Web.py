import RPi.GPIO as GPIO
import web
import sys
from Kontroler import NitSve
import os


urls = (
	'/start', 'pokreni',
	'/stop' , 'stani'
)

class pokreni:
	def GET(self):
		nit = NitSve()
		nit.start()	
		print "Zahtev!"
		return "Pokrenuta skripta"

class stani:
	def GET(self):
		nit = NitSve()
		nit.zaustavi()
		print "Skripta zaustavljena"				
		return "Skripta zaustavljena"

try:
	if __name__ == "__main__":			
		app = web.application(urls, globals())
		app.run()

except:
	print "Quit"
	GPIO.cleanup()


import pyfirmata
import urllib2
from threading import Timer
import time
import random

def send_sensor(val):
	response = urllib2.urlopen('http://127.0.0.1:8080/?sensor='+str(val))
	#html = response.read()
	#print html

 
def _timer():
	val=random.randrange(10)
	print "From print_time", time.time(), 'value', val

	send_sensor(val)
	Timer(1, _timer, ()).start()
Timer(1, _timer, ()).start()
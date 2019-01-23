import pyfirmata
import urllib2
from threading import Timer
import time
import random
import atexit


from pyfirmata import Arduino, util
board = Arduino('com23')
it = util.Iterator(board)
it.start()
a_0 = board.get_pin('a:0:i')
a_1 = board.get_pin('a:1:i')
d_2 = board.get_pin('d:2:i')


def salir():
    board.exit()
atexit.register(salir)

def send_sensor(val1,val2,val3):
	try:
		response = urllib2.urlopen('http://127.0.0.1:8080/?sensor1='+str(val1)+'&sensor2='+str(val2)+'&sensor3='+str(val3))
	#html = response.read()
	#print html
	except:
		pass
 
def _timer():
	val1=a_0.read()
	val2=a_1.read()
	val3=d_2.read()
	print "From print_time", time.time(), 'value', str(val1),str(val2),str(val3)

	send_sensor(val1,val2,val3)
	Timer(0.5, _timer, ()).start()
Timer(0.5, _timer, ()).start()

# Light Dependent Resistor

import time, sqlite3, threading
from Adafruit_ADS1x15 import *

global run
run = True

def log(voltage):
	cur.execute("insert into light values (datetime('now'), (?))", (voltage,))
	con.commit()
	
def worker():
	global con, cur, voltage
	adc = ADS1x15()
	gain = 4096
	sps = 250
	
	#Set up database connection
	con = sqlite3.connect("weather.db")
	cur = con.cursor()
	
	while (run):
		volts = adc.readADCSingleEnded() / 1000
		print "voltage: %.3f" % volts
		log(volts)
		time.sleep(5)

	con.close()
	return
	
#start thread
collectionThread = threading.Thread(target=worker)
collectionThread.daemon = True
collectionThread.start()
print "Collecting data..."

while(True):
    #Keep it going
    pass

#end loop so con will close
run = False
collectionThread.join()

#done

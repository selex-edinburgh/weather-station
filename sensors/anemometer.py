from Adafruit_MCP230xx import *
import time, sqlite3, threading

global run
run = True

def log(windspeed):
	cur.execute("insert into windspeed values(datetime('now'), (?))", (windspeed,))
	con.commit()
	
def worker():
	global cur, con
	mcp = Adafruit_MCP230XX(address = 0X20, num_gpios = 16)
	mcp.pullup(0, 1)
	
	#Set up database connection
	con = sqlite3.connect("weather.db")
	cur = con.cursor()
	print "Connected to database ok."
	
	while(run):
		
		start = time.time()
		pulses = -1
		# run for ten seconds
		while (time.time() < start + 10) :
			# wait for press or time up
			while (mcp.input(0) != 0 and time.time() < start + 10) :
				continue
			# count if press but not if we got here because time up
			if (mcp.input(0) == 0) :
				pulses = pulses + 1 # count the press
			# wait for release or time up
			while (mcp.input(0) == 0 and time.time() < start + 10) :
					continue
		print "number of pulses is %f" % pulses
		#Once per second (10 clicks) = 1.492mph
		# 1 click is 0.1492mph
		windspeed = pulses * 0.1492
		print "windspeed: {0:.2f}mph".format(windspeed)
		log(windspeed)
	con.close()
	

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

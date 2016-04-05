# Temperature and Pressure

from Adafruit_BMP085 import *
import sqlite3
import threading
import time

global run
run = True

#function for committing readings to the sqllte database
def log(temperature, pressure):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    cur.execute("INSERT INTO temps_values values(datetime('now'),(?))",(temperature,))
    cur.execute("INSERT INTO pressure_values values(datetime('now'),(?))",(pressure,))
    con.commit()
    con.close()

def worker():
    global con, cur, pressure, temperature
    
    #Set up database connection
    #con = sqlite3.connect("weather.db")
    #cur = con.cursor()
    #print "Connected to database ok."

    tempchip = BMP085(0x77)
    
    while(run):

        temp = tempchip.readTemperature()
        pressure = tempchip.readPressure()

        # convert pressure from Pascals to Millibar
        # 1 mbar = 1 hPA = 100Pa.
        pressure = pressure / 100

        #store temperature and pressure
        log(temp, pressure)

        print temp
        #sleep
        time.sleep(1)

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


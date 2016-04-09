# Wind Direction
# Connect black wire from wind vane to ground
# Connect green wire from wind vane to A0 on ADS1015 board
# Connect a 10K resistor from the green wire to +3.3V
# (the voltages below will need to be changed if you use +5V instead)
import sqlite3
import time
from Adafruit_ADS1x15 import *

adc = ADS1x15()

gain = 4096
sps = 250

def log(dir):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    cur.execute("INSERT INTO winddir values(datetime('now'),(?))",(dir,))
    con.commit()
    con.close()
    
while (True):
    volts = adc.readADCSingleEnded(0) / 1000
    print "voltage: %.3f" % volts
    if (volts < 0.45):
        print "W"
        log("W") 
    elif (volts < 0.9):
        print "NW"
        log("NW") 
    elif (volts < 1.35):
        print "N"
        log("N") 
    elif (volts < 1.75):
        print "SW"
        log("SW") 
    elif (volts < 2.25):
        print "NE"
        log("NE") 
    elif (volts < 2.70):
        print "S"
        log("S") 
    elif (volts < 2.95):
        print "SE"
        log("SE") 
    elif (volts < 3.2):
        print "E"
        log("E") 
    else:
        print "unknown"
           
    time.sleep(1)

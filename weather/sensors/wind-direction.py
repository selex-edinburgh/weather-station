# Wind Direction
# Connect black wire from wind vane to ground
# Connect green wire from wind vane to A0 on ADS1015 board
# Connect a 10K resistor from the green wire to +3.3V
# (the voltages below will need to be changed if you use +5V instead)

import time, sqlite3, threading
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
    volts = adc.readADCSingleEnded(1) / 1000
    print "voltage: %.3f" % volts
    if (volts > 0 and volts < 0.299):
        log("Unknown")
    elif (volts >= 0.3 and volts < 0.699):
        log("E")
    elif (volts >= 0.7 and volts < 1.099):
        log("SE")
    elif (volts >= 1.1 and volts < 1.799):
        log("S")
    elif (volts >= 1.8 and volts < 2.499):
        log("NE")
    elif (volts >= 2.5 and volts < 3.299):
        log("SW")
    elif (volts >= 3.3 and volts < 3.799):
        log("N")
    elif (volts >= 3.8 and volts < 3.999):
        log("NW")
    elif (volts >= 4.0):
        log("W")
    else:
        pass
    time.sleep(1)

#Done

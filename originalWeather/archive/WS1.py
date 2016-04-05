from Adafruit_MCP230xx import *
import time
mcp = Adafruit_MCP230XX(address = 0X20, num_gpios = 16)
mcp.pullup(4, 1)
pulses = 0
start = time.time()
import time
from Adafruit_ADS1x15 import *
adc = ADS1x15()
volts = adc.readADCSingleEnded(0) / 1000
gain = 4096
sps = 250

while (True):
    (time.time() < start + 1)
    
    while (mcp.input(4) != 0) :
        continue
    if (mcp.input(4) == 0):
        pulses = pulses + 1
    while (mcp.input(4) == 0) :
        print "%.1f revolutions since start" % (pulses / 2)
        continue
    if (volts < 0.45):
        print "W"
    elif (volts < 0.9):
        print "NW"
    elif (volts < 1.35):
        print "N"
    elif (volts < 1.75):
        print "SW"
    elif (volts < 2.25):
        print "NE"
    elif (volts < 2.70):
        print "S"
    elif (volts < 2.95):
        print "SE"
    elif (volts < 3.2):
        print "E"
    else:
        print "unknown"

    

    


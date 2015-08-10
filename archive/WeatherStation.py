
# Example of testing switches

from Adafruit_MCP230xx import *
import time
from Adafruit_ADS1x15 import *

adc = ADS1x15()

gain = 4096
sps = 250

mcp = Adafruit_MCP230XX(address = 0X20, num_gpios = 16)

mcp.pullup(4, 1)

while (True):

    # wait for button press
    while (mcp.input(4) != 0):
        continue

    # delay 10ms to allow switch "bounce" to settle
    time.sleep(0.01)

    print "Switch pressed"

    # wait for button release
    while (mcp.input(4) == 0):
        continue
    
    # delay 10ms to allow switch "bounce" to settle
    time.sleep(0.01)

    print "Switch released"


pulses = 0

start = time.time()

while (time.time() < start + 10):

    while (mcp.input(0) != 0 and time.
           time() < start + 10):
        continue
    if (mcp.input(0) == 0):
        pulses = pulses + 1

    while (mcp.input(0) == 0):
        continue

adc = ADS1x15()

gain = 4096
sps = 250

while (True):
    volts = adc.readADCSingleEnded(0) / 1000
    # print "voltage: %.3f" % volts
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

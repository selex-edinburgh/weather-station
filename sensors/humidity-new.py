from Adafruit_ADS1x15 import *
import time

adc = ADS1x15()
gain = 4096
sps = 250

Humidity_Voltage = adc.readADCSingleEnded(2)/1000
print Humidity_Voltage

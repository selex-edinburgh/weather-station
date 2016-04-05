from Adafruit_BMP085 import *
from Adafruit_ADS1x15 import *
import time

tempchip = BMP085(0x77)

adc = ADS1x15()
gain = 4096
sps = 250


#Attempt to read temperature
temp= tempchip.readTemperature()
#Use temperature to find humidity
humidity = adc.readADCSingleEnded(0)/1000 #eh screw it just print them for now

print "temp %.2fC , %.3f volts" % (temp, humidity)

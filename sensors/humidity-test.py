from Adafruit_ADS1x15 import *
from math import *
import time


adc = ADS1x15()
gain = 4096
sps = 250
input_voltage = 3.3
temp = 20

humidity_voltage = adc.readADCSingleEnded(2)/1000
print humidity_voltage

impedance = (humidity_voltage / (input_voltage - humidity_voltage)) * 10000
print impedance

if temp <= 10:
                    if impedance > 9900:
                        humidity = 20
                    if impedance <= 9900 and impedance > 4400:
                        humidity = 25
                    if impedance <= 4400 and impedance > 1900:
                        humidity = 30
                    if impedance <= 1900 and impedance > 810:
                        humidity = 35
                    if impedance <= 810 and impedance > 420:
                        humidity = 40
                    if impedance <= 420 and impedance > 211:
                        humidity = 45
                    if impedance <= 211 and impedance > 109:
                        humidity = 50
                    if impedance <= 109 and impedance > 63:
                        humidity = 55
                    if impedance <= 63 and impedance > 37:
                        humidity = 60
                    if impedance <= 37 and impedance > 22:
                        humidity = 65
                    if impedance <= 22 and impedance > 14:
                        humidity = 70
                    if impedance <= 14 and impedance > 9:
                        humidity = 75
                    if impedance <= 9 and impedance > 6:
                        humidity = 80
                    if impedance <= 6 and impedance > 4:
                        humidity = 85
                    if impedance <= 4:
                        humidity = 90
elif temp >= 10 and temp < 15:
                    if impedance > 6900:
                        humidity = 20
                    if impedance <= 6900 and impedance > 3100:
                        humidity = 25
                    if impedance <= 3100 and impedance > 1400:
                        humidity = 30
                    if impedance <= 1400 and impedance > 600:
                        humidity = 35
                    if impedance <= 600 and impedance > 300:
                        humidity = 40
                    if impedance <= 300 and impedance > 150:
                        humidity = 45
                    if impedance <= 150 and impedance > 83:
                        humidity = 50
                    if impedance <= 83 and impedance > 48:
                        humidity = 55
                    if impedance <= 48 and impedance > 28:
                        humidity = 60
                    if impedance <= 28 and impedance > 17:
                        humidity = 65
                    if impedance <= 17 and impedance > 12:
                        humidity = 70
                    if impedance <= 12 and impedance > 7.3:
                        humidity = 75
                    if impedance <= 7.3 and impedance > 4.8:
                        humidity = 80
                    if impedance <= 4.8 and impedance > 3.2:
                        humidity = 85
                    if impedance <= 3.2:
                        humidity = 90
elif temp >= 15 and temp < 20:
                    if impedance > 4600:
                        humidity = 20
                    if impedance <= 4600 and impedance > 2000:
                        humidity = 25
                    if impedance <= 2000 and impedance > 900:
                        humidity = 30
                    if impedance <= 900 and impedance > 430:
                        humidity = 35
                    if impedance <= 430 and impedance > 220:
                        humidity = 40
                    if impedance <= 220 and impedance > 110:
                        humidity = 45
                    if impedance <= 110 and impedance > 62:
                        humidity = 50
                    if impedance <= 62 and impedance > 37:
                        humidity = 55
                    if impedance <= 37 and impedance > 22:
                        humidity = 60
                    if impedance <= 22 and impedance > 14:
                        humidity = 65
                    if impedance <= 14 and impedance > 9.4:
                        humidity = 70
                    if impedance <= 9.4 and impedance > 6:
                        humidity = 75
                    if impedance <= 6 and impedance > 3.9:
                        humidity = 80
                    if impedance <= 3.9 and impedance > 2.7:
                        humidity = 85
                    if impedance <= 2.7:
                        humidity = 90
elif temp >= 20 and temp < 25:
                    if impedance > 3200:
                        humidity = 20
                    if impedance <= 3200 and impedance > 1500:
                        humidity = 25
                    if impedance <= 1500 and impedance > 670:
                        humidity = 30
                    if impedance <= 670 and impedance > 310:
                        humidity = 35
                    if impedance <= 310 and impedance > 160:
                        humidity = 40
                    if impedance <= 160 and impedance > 83:
                        humidity = 45
                    if impedance <= 83 and impedance > 48:
                        humidity = 50
                    if impedance <= 48 and impedance > 29:
                        humidity = 55
                    if impedance <= 29 and impedance > 18:
                        humidity = 60
                    if impedance <= 18 and impedance > 12:
                        humidity = 65
                    if impedance <= 12 and impedance > 7.8:
                        humidity = 70
                    if impedance <= 7.8 and impedance > 5:
                        humidity = 75
                    if impedance <= 5 and impedance > 3.3:
                        humidity = 80
                    if impedance <= 3.3 and impedance > 2.2:
                        humidity = 85
                    if impedance <= 2.2:
                        humidity = 90
elif temp >= 25 and temp < 30:
                    if impedance > 2300:
                        humidity = 20
                    if impedance <= 2300 and impedance > 920:
                        humidity = 25
                    if impedance <= 920 and impedance > 450:
                        humidity = 30
                    if impedance <= 450 and impedance > 220:
                        humidity = 35
                    if impedance <= 220 and impedance > 120:
                        humidity = 40
                    if impedance <= 120 and impedance > 66:
                        humidity = 45
                    if impedance <= 66 and impedance > 37:
                        humidity = 50
                    if impedance <= 37 and impedance > 23:
                        humidity = 55
                    if impedance <= 23 and impedance > 14:
                        humidity = 60
                    if impedance <= 14 and impedance > 9.6:
                        humidity = 65
                    if impedance <= 9.6 and impedance > 6.5:
                        humidity = 70
                    if impedance <= 6.5 and impedance > 4.2:
                        humidity = 75
                    if impedance <= 4.2 and impedance > 2.8:
                        humidity = 80
                    if impedance <= 2.8 and impedance > 1.9:
                        humidity = 85
                    if impedance <= 1.9:
                        humidity = 90
elif temp >= 30:
                    if impedance > 1700:
                        humidity = 20
                    if impedance <= 1700 and impedance > 770:
                        humidity = 25
                    if impedance <= 770 and impedance > 360:
                        humidity = 30
                    if impedance <= 360 and impedance > 170:
                        humidity = 35
                    if impedance <= 170 and impedance > 90:
                        humidity = 40
                    if impedance <= 90 and impedance > 51:
                        humidity = 45
                    if impedance <= 51 and impedance > 29:
                        humidity = 50
                    if impedance <= 29 and impedance > 18:
                        humidity = 55
                    if impedance <= 18 and impedance > 12:
                        humidity = 60
                    if impedance <= 12 and impedance > 8:
                        humidity = 65
                    if impedance <= 8 and impedance > 5.5:
                        humidity = 70
                    if impedance <= 5.5 and impedance > 3.8:
                        humidity = 75
                    if impedance <= 3.8 and impedance > 2.5:
                        humidity = 80
                    if impedance <= 2.5 and impedance > 1.7:
                        humidity = 85
                    if impedance <= 1.7:
                        humidity = 90
print humidity

"""
#This is an equation which roughly shows the relationship between temperature, impedance and humidity(still in trial)
humidity = 108.3 - (20 * log(temp)) - (17.1 * log(impedance)) - (3.99 / temp) + (30.73 / impedance)
print humidity
"""


                               

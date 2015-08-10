import os, time
from Adafruit_MCP230xx import *
mcp = Adafruit_MCP230XX(address = 0X20, num_gpios = 16)
mcp.config(7,mcp.OUTPUT)

#Start all scripts
os.system("sudo python %s &" % ("weather/flaskr/weather.py"))
os.system("sudo python %s &" % ("raingauge.py"))
os.system("sudo python %s &" % ("temperature-pressure.py"))
os.system("sudo python %s &" % ("anemometer.py"))
os.system("sudo python %s &" % ("LDR.py"))

err = [0, 0, 0, 0, 0]
while (True):
	
	for e in err:
		if e == 1:
			mcp.output(7,1)
			time.sleep(0.2)
			mcp.output(7,0)
			time.sleep(0.2)
	
	tmp = os.popen("ps -Af").read()
	if "weather.py" not in tmp[:]:
		err[0] = 1
	else:
		err[0] = 0
	if "raingauge.py" not in tmp[:]:
		err[1] = 1
	else:
		err[1] = 0
	if "temperature-pressure.py" not in tmp[:]:
		err[2] = 1
	else:
		err[2] = 0
	if "anemometer.py" not in tmp[:]:
		err[3] = 1
	else:
		err[3] = 0
	if "LDR.py" not in tmp[:]:
		err[4] = 1
	else:
		err[4] = 0
	time.sleep(5)

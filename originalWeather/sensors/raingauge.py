#!/usr/bin/python

from Adafruit_MCP230xx import *
import sys
import os
import time
import sqlite3
import threading 

INPUT = 0
mcp = Adafruit_MCP230XX(address = 0x20, num_gpios = 16)
mcp.pullup(INPUT,1)
global run
run = True

#function for committing readings to the sqlite database
def log(inches):
    cur.execute("INSERT INTO rainfall values(datetime('now'),(?))",(inches,))
    con.commit()

def collect():
    global start, average, rainfall, clicks, iterations, INCHES_PER_CLICK, con, cur
    iterations = 1
    INCHES_PER_CLICK = 0.011
    start = time.time()
    average = 0
    rainfall = 0
    clicks = 0

    #Set up database connection
    con = sqlite3.connect("weather.db")
    cur = con.cursor()

    while(run):
        #Thread worker function
        #Gather data
        if(mcp.input(INPUT) == 0):
            clicks += 1
            #debug-reassure me that clicking is happening
            #sys.stdout.write("click!")
            #sys.stdout.flush()

        #print if the time is the right interval from the start time
        #in practice, you would want to transmit this to the other pi instead.
        if(time.time() - start > 60):
            #Calculate total rainfall
            rainfall += clicks * INCHES_PER_CLICK
            #Get average
            average = rainfall / iterations
            #print
            output = "\nToday's rainfall: %.2fin, minute average: %.2fin\n" % (rainfall, average)
            sys.stdout.write(output)
            sys.stdout.flush()
            #log to database
            log(clicks * INCHES_PER_CLICK)
            #reset start time
            start = time.time()
            clicks = 0
            iterations += 1

        #if it has been more than a day, reset the total rainfall & average
        if(time.time() - start > 60*60*24):
            average = 0
            rainfall = 0
            iterations = 1
            start = time.time()

        time.sleep(0.3) #avoid switch bounce

        
    #close the database connection    
    con.close()
    return

#start thread
collectionThread = threading.Thread(target=collect)
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

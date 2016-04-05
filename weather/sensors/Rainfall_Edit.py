from Adafruit_MCP230xx import *
import time, sqlite3, threading

global run
run = True

def log(inches):
    con = sqlite3.connect("weather.db")
    cur = con.cursor()
    cur.execute("INSERT INTO rainfall_values values(datetime('now'),(?))",(inches,))
    con.commit()
    con.close()
        
def worker():
        global cur, con, inches
        mcp = Adafruit_MCP230XX(address = 0X20, num_gpios = 16)
        mcp.pullup(5, 1)

        #measurement period for while loop in seconds
        mperiod = 10 
        
        iterations = 1
        accumulation = 0
        total_clicks = 0
        
        #Set up database connection
        #con = sqlite3.connect("weather.db")
        #cur = con.cursor()
        print "Connected to database ok.\n"
        
        while(run):

                start = time.time()
                clicks = 0
                inch = 0
                rainfall = 0
                
                # run for 1 minute (when debugged set mperiod to 60)
                while (time.time() < start + mperiod) :
                        # wait for press or time up
                        while (mcp.input(5) != 0 and time.time() < start + mperiod) :
                                continue
                        # count if press but not if we got here because time up
                        if (mcp.input(5) == 0) :
                                clicks = clicks + 1 # count the press
                        # wait for release or time up
                        while (mcp.input(5) == 0 and time.time() < start + mperiod) :
                                continue
                        
                #  Each click represents 0.011 Inches of rainfall.
                inch = clicks * 0.011
                rainfall = inch/iterations
                accumulation = accumulation + rainfall

                total_clicks = total_clicks + clicks
                
                print "number of clicks is %f" % clicks
                print "Inches of rain: {0:.3f} Inches".format(inch)
                print "total rainfall: {0:.3f} Inches".format(accumulation)
                print "total clicks %f" % total_clicks
                print

                inchRF = inch
                
                log(inchRF)
                
                if (time.time() - start > 60*60*24):
                    clicks = 0
                    inch = 0
                    rainfall = 0
                    accumulation = 0
                    total_clicks = 0
                    start = time.time()
                    
                #con.commit()
                
        con.close()
        

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

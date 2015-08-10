import sqlite3

from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
    
DATABASE = '/home/pi/weather.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

	
@app.before_request
def before_request():
	g.db = connect_db()
	
@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

@app.route('/')
def hello():
	lr = 1433751407 #last rainfall timestamp
	cur = g.db.execute('select strftime(\'%H:%M\', timestamp), inches, timestamp from rainfall')
	entries = [dict(timestamp=row[0], inches=row[1]) for row in cur.fetchall()]
	cur = g.db.execute('select strftime(\'%H:%M\', timestamp), inches, timestamp from rainfall')
	for row in cur.fetchall():
		if row[1] > 0:
			lr = row[2]
	cur = g.db.execute("select strftime('%s', 'now')-strftime('%s','{}')".format(lr))
	lr = cur.fetchone()[0] / 60 # lr is now the number of minutes since last rainfall
	cur = g.db.execute("select sum(inches) from rainfall where timestamp > datetime('now', '-24 hours')")
	rainfalltoday = cur.fetchone()[0]
	if rainfalltoday == None:
		rainfalltoday = 0
	#produce a dictionary of the last 24 hourly rainfall values for the chart, even if there is no data
	rcvalues = [dict() for i in range(23)]
	for i in range(0, 23):
	    cur = g.db.execute("select sum(inches) from rainfall where timestamp > datetime('now', '-{} hours') and timestamp < datetime('now', '-{} hours')".format(i+1, i))
	    val = cur.fetchone()[0]
	    if val == None:
			val = 0
	    rcvalues[i] = dict(inches=val, iden = i)
	    
	# Temperature
	#Latest temperature in degrees
	cur = g.db.execute("select temp from temps order by timestamp limit 1")
	curtemp = cur.fetchone()[0]
	#Max/min today
	cur = g.db.execute("select min(temp), max(temp) from temps")
	minmax = {0, 0}
	minmax = cur.fetchone()
	
	#Wind
	#Current Windspeed
	cur = g.db.execute("select avg(windspeed) from windspeed where timestamp > datetime('now','-5 minutes')")
	curwindspeed = cur.fetchone()[0]
	if curwindspeed == None:
		curwindspeed = 0.0
		
	#Light level
	cur = g.db.execute("select avg(voltage) from light where timestamp > datetime('now', '-2 minutes')")
	lightlevel = cur.fetchone()[0]
	if lightlevel == None:
		cur = g.db.execute("select voltage from light order by timestamp desc limit 1")
		lightlevel = cur.fetchone()[0]
		
	return render_template('main.html',entries=entries, rainfalltoday=rainfalltoday, lr=lr, rcvalues=rcvalues, \
		curtemp = curtemp, minmax=minmax, curwindspeed = curwindspeed, lightlevel=lightlevel)
	
if __name__ == '__main__':
	app.run(host='0.0.0.0')
	

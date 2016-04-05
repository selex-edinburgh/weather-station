import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
    

DATABASE = 'flaskr.db'
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
	cur = g.db.execute('select datetime, inches from entries')
	entries = [dict(datetime=row[0], inches=row[1]) for row in cur.fetchall()]
	return render_template('show_entries.html',entries=entries)
	
if __name__ == '__main__':
	app.run()
	
@app.route('/add',methods=['POST'])
def add_entry():
	g.db.execute('insert into entries (datetime, inches) values (?, ?)',
	        [1433422142, 1])
	g.db.commit()
	flash('New entry was successfully posted')
	return redirect(url_for('show_entries'))

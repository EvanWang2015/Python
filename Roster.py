import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#Setup 
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE
);

CREATE TABLE Course(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT UNIQUE
);

CREATE TABLE Member(
	user_id INTEGER,
	course_id INTEGER,
	role INTEGER,
	PRIMARY KEY (user_id, course_id)
);
''')

fname = input('Input file name: ')
if (len(fname)<1): fname = 'roster_data.json'
print(fname)
data = open(fname).read()
json_data = json.loads(data)
if json_data is None:
	print('Fail to retrieve')
count = 0
for entry in json_data:
	name = entry[0]
	course = entry[1]
	role = entry[2]
	cur.execute('INSERT OR IGNORE INTO User (name) VALUES(?)', (name,))
	cur.execute('SELECT id FROM User WHERE name = ?', (name,))
	user_id = cur.fetchone()[0]
	
	cur.execute('INSERT OR IGNORE INTO Course (title) VALUES(?)',(course,))
	cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
	course_id = cur.fetchone()[0]
	
	cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) 
		VALUES( ?, ?, ?)''', (user_id, course_id, role))
	
conn.commit()	



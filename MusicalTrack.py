import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('MusicTrackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE
);

CREATE TABLE Genre(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE
);

CREATE TABLE Album(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id INTEGER,
	title TEXT UNIQUE
);

CREATE TABLE Track (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT UNIQUE,
	album_id INTEGER,
	genre_id INTEGER,
	len INTEGER,
	rating INTEGER,
	counting INTEGER
);
''')

fname = input('Enter file name: ')
if(len(fname)<1): fname = 'Library.xml'

#<key>Track ID</key><integer>369</integer>
#<key>Name</key><string>Another one bites the dust</string>
#<key>Artist</key><string>Queen</string>

def lookup(d,key):
	found = False
	for child in d:
		if found: return child.text
		if child.tag =='key' and child.text == key:
			found = True
	return None
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count: ', len(all))	
for entry in all:
	if(lookup(entry, 'Track ID') is None): continue
	name = lookup(entry, 'Name')
	artist = lookup(entry,'Artist')
	album = lookup(entry,'Album')
	count = lookup(entry,'Play Count')
	rating = lookup(entry,'Rating')
	length = lookup(entry,'Total Time')
	genre = lookup(entry, 'Genre')
	
	if name is None or artist is None or album is None or genre is None:
		continue
		
	cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES(?)', (artist,))
	cur.execute('SELECT id from Artist WHERE name = ?',(artist,))
	
	artist_id = cur.fetchone()[0]
	
	cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES(?)', (genre,))
	cur.execute('SELECT id from Genre WHERE name = ?',(genre,))
	genre_id = cur.fetchone()[0]
	
	cur.execute('INSERT OR IGNORE INTO Album (artist_id, title) VALUES(?,?)',(artist_id, album))
	cur.execute('SELECT id from Album where title = ?',(album,))
	album_id = cur.fetchone()[0]
	
	cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, counting) 
		VALUES( ?, ?, ?, ?, ?, ?)''',(name, album_id, genre_id, length, rating, count))
	
conn.commit()

import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if(len(fname)<1):fname = 'mbox.txt'
fh = open(fname)
#count = 0
for line in fh:	
	if not line.startswith('From: '): continue
	#print(line)
	pieces = line.split()
	email = pieces[1].split('@')
	#print (email)
	domain = email[1]
	#print(domain[0], '', domain[1])

	cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts(org, count) VALUES (?,1)''',(domain,))
	else:
		cur.execute('UPDATE Counts SET count=count+1 WHERE org =?',(domain,))
		
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER By Count DESC LIMIT 10'

print("Counts:")
for row in cur.execute(sqlstr):
	print(str(row[0]),row[1])

cur.close()


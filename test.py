import MySQLdb

db = MySQLdb.connect("glapeira.freeboxos.fr", "cedric", "cedb002", "elevage")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()


# Use all the SQL you like
cur.execute("SELECT * from Animal")

# print all the first cell of all the rows
for row in cur.fetchall():
	print row[0]

db.close()

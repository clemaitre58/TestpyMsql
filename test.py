import MySQLdb

db = MySQLdb.connect("xxxxxxx.freeboxos.fr", "xxxxx", "xxxx", "elevage")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * Animal")

# print all the first cell of all the rows
#for row in cur.fetchall():
#        print row[0]

db.close()

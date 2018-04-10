# OpenOPC and SQLite Python example
import sqlite3
import os
import time
import OpenOPC
dbfile=¡¯test.db¡¯
remotehost=¡¯testbox¡¯
opcserver=¡¯Matrikon.OPC.Simulation¡¯
tagname=¡¯Random.Int4¡¯
sampletime = 2
dbexist = os.path.exists(dbfile)
db = sqlite3.connect(dbfile)
cur = db.cursor()
# create table first time new database is accessed
if not dbexist:
    sqlstring = 'CREATE TABLE opcdata \
    (id INTEGER PRIMARY KEY, tag TEXT, \
    val TEXT, stat TEXT, datetime TEXT, atime TEXT)'
    cur.execute(sqlstring)
    db.commit()
while 1>0: # infinite loop kill with Ctrl-C
    opc=OpenOPC.client()
    opc.connect(opcserver,remotehost)
    (opcvalue,opcstat,opctime) = opc.read(tagname)
    opc.close()
    atime = time.asctime() # current computer time as float
    sqlstring = 'INSERT INTO opcdata (id, tag, val, stat, datetime, atime) \
    VALUES(NULL, "%s", "%f", "%s", "%s", "%s")'\
    %(tagname,opcvalue,opcstat,opctime,atime)
    cur.execute(sqlstring)
    db.commit()
    cur.execute('SELECT * FROM opcdata')
    dbvalues = cur.fetchall()
    dblen = len(dbvalues)
    print (dbvalues[dblen-1]) # print newest value in database
time.sleep(sampletime)
# end of while loop
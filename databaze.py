__author__ = 'mat'
__author__ = 'student'
import sqlite3 as lite
import sys
from datetime import datetime, timedelta


def napeti_pole():
    try:
        con = lite.connect('test.db')
        with con:
            con.row_factory = lite.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM udaje_clanky")

            rows = cur.fetchall()
            
            return rows

    except lite.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:

        if con:
            con.close()

    return 0



def napln_db():
    try:
        con = lite.connect('test.db')
        with con:
            cur = con.cursor()
            try:
                cur.execute('SELECT * FROM udaje_clanky')
            except lite.Error, e:
                cur.execute("CREATE TABLE udaje_clanky(clanek INT, hodnota INT)")
            for i in range(1,17):
                cur.execute("INSERT INTO udaje_clanky(clanek,hodnota) VALUES(?,?)",(i,3000-i))

    except lite.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:

        if con:
            con.close()

    return 0
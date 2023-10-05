import sqlite3
import csv
from openpyxl import Workbook

def populateDb(data):
    for row in data:
        cur.executemany("INSERT INTO timeAttendance VALUES(?,?,?,?,?)",(row,))
        #print(row)

        
con = sqlite3.connect('register.db')
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS timeAttendance''')
cur.execute('''CREATE TABLE timeAttendance(userID INTEGE R NOT NULL, date TEXT
            NOT NULL, time TEXT NOT NULL, staff TEXT NOT NULL, io TEXT)''')

dataFile = open('Time and attendance.csv')
inputData = list(csv.reader(dataFile))

populateDb(inputData)

cur.execute('''SELECT * FROM timeAttendance ORDER BY userID''')

users = cur.execute('''SELECT userID FROM timeAttendance GROUP BY userID''')

user = users.fetchall()[0][0]

cur.execute('''SELECT * FROM timeAttendance WHERE userID = ?''', (user,))

##for user in users.fetchall():
print(cur.fetchall())

dataFile.close()
con.commit()
con.close()
        

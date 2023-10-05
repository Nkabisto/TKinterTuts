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

users = cur.execute('''SELECT userID,staff FROM timeAttendance GROUP BY userID''')

userIDs = users.fetchall()

for user in userIDs:
    cur.execute('''SELECT * FROM timeAttendance WHERE userID = ?''', (user[0],))

##for user in users.fetchall():
print(userIDs)

dataFile.close()
con.commit()
con.close()
        

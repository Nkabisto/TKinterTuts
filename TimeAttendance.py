import sqlite3
#from openpyxl import Workbook

def populateDb(dataFile):
    with open(dataFile + '.txt','r') as file:
        print('AC.No','Date','Time','Staff')
        for line in file:
            newLine = line.split()
            row = [newLine[0],newLine[1],newLine[2],newLine[5]]
            cur.executemany("INSERT INTO timeAttendance VALUES(?,?,?,?)", (row,))


def createTimeAndAttendanceTable():
    cur.execute('''DROP TABLE IF EXISTS timeAttendance''')
    cur.execute('''CREATE TABLE timeAttendance(ac_no INTEGER NOT NULL, date TEXT
            NOT NULL, time TEXT NOT NULL, staff TEXT NOT NULL)''')
        
con = sqlite3.connect('register.db')
cur = con.cursor()

createTimeAndAttendanceTable(); #CREATE TABLE timeAttendance

INPUTFILE = 'testing'
populateDb(INPUTFILE)

emp = cur.execute('''SELECT * FROM timeAttendance ORDER BY ac_no''')

for r in emp.fetchall():
    print(list(r))

con.commit()
con.close()



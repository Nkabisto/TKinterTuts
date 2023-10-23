import sqlite3
#from openpyxl import Workbook

def populateDb(dataFile):
    with open(dataFile + '.txt','r') as file:
        print('AC.No','Date','Time','Staff')
        for line in file:
            newLine = line.split()
            ac_no = newLine[0]
            cdate = newLine[1]
            ctime = newLine[2]
            staff = newLine[5]
            print(ac_no,cdate,ctime,staff)


def createTimeAndAttendanceTable():
    cur.execute('''DROP TABLE IF EXISTS timeAttendance''')
    cur.execute('''CREATE TABLE timeAttendance(ac_no INTEGER NOT NULL, date TEXT
            NOT NULL, time TEXT NOT NULL, staff TEXT NOT NULL, io TEXT)''')
        
con = sqlite3.connect('register.db')
cur = con.cursor()

createTimeAndAttendanceTable(); #CREATE TABLE timeAttendance

INPUTFILE = 'testing'
populateDb(INPUTFILE)
con.commit()
con.close()



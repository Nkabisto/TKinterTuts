import sqlite3
#from openpyxl import Workbook
import re

def populateDb(dataFile):
    with open(dataFile + '.txt','r') as file:
        #print('AC.No','Date','Time','Staff')
        for line in file:
            newLine = line.split()
            row = [newLine[0],newLine[1],newLine[2],newLine[5]]
            dataValidation(row[0],row[1],row[2],row[3])
            cur.executemany("INSERT INTO timeAttendance VALUES(?,?,?,?)", (row,))


def createTimeAndAttendanceTable():
    cur.execute('''DROP TABLE IF EXISTS timeAttendance''')
    cur.execute('''CREATE TABLE timeAttendance(ac_no INTEGER NOT NULL, date TEXT
            NOT NULL, time TEXT NOT NULL, staff TEXT NOT NULL)''')

def dataValidation(acNo,date,time,name):
    if not isStaffIDCorrect(acNo):
        raise Exception('Staff no.: ' + acNo + ' is incorrect')

    if not isDateCorrect(date):
        raise Exception('Date: ' + date + ' is incorrect')
##
##    if not isTimeCorrect(ctime):
##        raise Exception('Time: ' + time + ' is incorrect')
##
##    if not isNameCorrect(name):
##        raise Exception('Staff label: ' + name + ' is incorrect')
    

def isStaffIDCorrect(staffID):
    return staffID.isdecimal()

def isDateCorrect(cdate):
    datePattern = r'\d{4}-\d{2}-\d{2}'
    dateRegex = re.compile(datePattern)
    match = dateRegex.search(cdate)
    return match != None
    
def isTimeCorrect(ctime):
    timePattern = r'\d{4}-\d{2}-\d{2}'
    timeRegex = re.compile(timePattern)
    match = timeRegex.search(cdate)
    return match != None

def isNameCorrect(name):
    return name.isalnum()

con = sqlite3.connect('register.db')
cur = con.cursor()

createTimeAndAttendanceTable(); #CREATE TABLE timeAttendance

INPUTFILE = 'testing'
populateDb(INPUTFILE)

cur.execute('''SELECT * FROM timeAttendance ORDER BY ac_no''')
emp = cur.execute('''SELECT ac_no, staff FROM timeAttendance GROUP BY ac_no''')

employees = emp.fetchall()

print(employees)

# Filter database by AC.No
##for e in employees:
##    cur.execute('''SELECT * FROM timeAttendance WHERE ac_no = ?''',(e[0])('2023-09-0
##    

con.commit()
con.close()



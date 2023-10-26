import sqlite3
from openpyxl import Workbook
import re

def populateDb(dataFile):
    with open(dataFile + '.txt','r') as file:
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

    if not isTimeCorrect(time):
        raise Exception('Time: ' + time + ' is incorrect')

    if not isNameCorrect(name):
        raise Exception('Staff label: ' + name + ' is incorrect')
    

def isStaffIDCorrect(staffID):
    return staffID.isdecimal()

def isDateCorrect(cdate):
    datePattern = r'\d{4}-\d{2}-\d{2}'
    dateRegex = re.compile(datePattern)
    match = dateRegex.search(cdate)
    return match != None
    
def isTimeCorrect(ctime):
    timePattern = r'\d{2}:\d{2}:\d{2}'
    timeRegex = re.compile(timePattern)
    match = timeRegex.search(ctime)
    return match != None

def isNameCorrect(name):
    return name.isalnum()

def staffDatesAndTimesDict(attendanceData):
    staffDict = {}
    for row in attendanceData:
        date = row[0]
        time = row[1]

        if date in staffDict.keys():
            staffDict[date] += ' ' + time
        else:
            staffDict[date] = time
    return staffDict
        

def printToExcelWb(acNo,name,inputDict,staffSheet):
    inputArray = list(inputDict.items())
    HEADERS = ['AC NO','NAME','DATE','TIME','COMMENTS']
    staffSheet.append(HEADERS)
    
    for row in inputArray:
        staffSheet.append([acNo,name] + list(row))
        

con = sqlite3.connect('register.db') # create a new database named register
cur = con.cursor()      

createTimeAndAttendanceTable() #CREATE TABLE timeAttendance

INPUTFILE = 'Time and attendance from 22 Sep to 24 October 2023'
populateDb(INPUTFILE)

cur.execute('''SELECT * FROM timeAttendance ORDER BY ac_no''')
emp = cur.execute('''SELECT ac_no, staff FROM timeAttendance GROUP BY ac_no''')

employees = emp.fetchall()

wb = Workbook()

# Filter database by employeeID number
for e in employees:
    staffID = e[0] 
    staffName = e[1]
    sheet = wb.create_sheet(staffName)

    cur.execute('''SELECT date,time FROM timeAttendance WHERE ac_no = ? ORDER by date,time''',(staffID,))

    staffDict = staffDatesAndTimesDict(cur.fetchall())    
    printToExcelWb(staffID,staffName,staffDict,sheet)

del wb['Sheet']
    

wb.save(INPUTFILE + '.xlsx')
con.commit()
con.close()


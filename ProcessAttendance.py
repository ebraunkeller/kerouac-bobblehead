# Process the attendance data by adding fields for day of week and school year and reoder the fields
# so that they match the enrollment file: date, lasid, status (ABS), day, school year
# also, clean the bad data. Many absence records are on days not in the calendar. Check the date
# of the absence against the calendar and delete bad records
import csv, time
from datetime import datetime

# convert X2 date format to Python format mm/dd/yyyy
def date_func(date):
    return date.split("/")[0].zfill(2)+"/"+date.split("/")[1].zfill(2)+"/"+date.split("/")[2]

def schoolyear(date):
    if int(date.split("/")[0]) <8 : return date.split("/")[2]
    else: return str(int(date.split("/")[2])+1)
    
def calday(date):
    cal_date = datetime.strptime(date_func(date),'%m/%d/%Y')
    return cal_date.strftime("%a")

AttFile = "C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\Attendance.csv"
OutFile = "C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\TableauFormat\ProcessedAttend.csv"
CalendFile ="C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\Calendar.csv"

csvfile=open(AttFile,'rb')
reader=csv.reader(csvfile)

Ccsvfile = open(CalendFile,'rb')
Creader = csv.reader(Ccsvfile)

with open(OutFile,'a+b') as csvout:
    wr=csv.writer(csvout,delimiter=',')
    wr.writerow(['Date','Lasid','Status','Day','SchoolYear']) 
# skip all the headers
    next(reader)
    for row in reader:
        output = [row[0],row[1],'ABS',calday(row[0]), schoolyear(row[0])]
        for crow in Creader:
            if crow[0] == row[0] :              
                if crow[1]=='TRUE': wr.writerow(output)
                break
        Ccsvfile.seek(0)
csvout.close()
csvfile.close()   
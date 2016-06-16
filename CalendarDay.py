# Open the calendar file, read it into memory.
# Pick a date, determine if it's a school day
# for now hardcode the file path and name
import csv, time, string,sys
from datetime import datetime

# convert X2 date format to Python format mm/dd/yyyy
def date(date):
    return date.split("/")[0].zfill(2)+"/"+date.split("/")[1].zfill(2)+"/"+date.split("/")[2] 

Calfile="C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\RawCalendar.csv"
Outfile="C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\NewCalendar.csv"

Wcsvfile = open(Outfile,'a+b')
wr= csv.writer(Wcsvfile, delimiter=',')

# Today = time.strftime("%m/%d/%Y") eventually
print sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]
YearOneStartDate = datetime.strptime(date(sys.argv[1]),'%m/%d/%Y')
YearOneEndDate   = datetime.strptime(date(sys.argv[2]),'%m/%d/%Y')
YearTwoStartDate = datetime.strptime(date(sys.argv[3]),'%m/%d/%Y')
YearTwoEndDate   = datetime.strptime(date(sys.argv[4]),'%m/%d/%Y')
ListYear1 =[]
ListYear2 =[]


csvfile =open(Calfile, 'rb')
reader = csv.reader(csvfile)

for row in reader:
    if row[1] == "TRUE":
        CalendarDay = datetime.strptime(date(row[0]),'%m/%d/%Y')
        if   YearOneStartDate <= CalendarDay <= YearOneEndDate: ListYear1.append(CalendarDay) 
        if YearTwoStartDate <= CalendarDay <= YearTwoEndDate:   ListYear2.append(CalendarDay)

ListYear1.sort()
ListYear2.sort()

ListAll=(ListYear1,ListYear2)

for stuff in ListAll:
    index =1
    for morestuff in stuff:
        Term='T4'
        if 1<= index <= 45: Term='T1'
        elif 46<= index <=90: Term='T2'
        elif 91<= index <=135: Term='T3'
    
        wrow = [morestuff.strftime('%m/%d/%Y'), 'TRUE',Term]
        wr.writerow(wrow)
        index+=1





                

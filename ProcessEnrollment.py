# Find students enrolled at some point in SY15-16, create an enrollment record for
# each day. This follows the Providence model where there is both an enrollment
# record and an absent record if the student was absent.
# The absense file is appended to the bottom of this file
# This uses PCG Enrollment  plus the calendar table which lists
# all the days of the year and whether or not they are school days.
#

import csv, time
from datetime import datetime

# convert X2 date format to Python format mm/dd/yyyy
def date(date):
    return date.split("/")[0].zfill(2)+"/"+date.split("/")[1].zfill(2)+"/"+date.split("/")[2] 
    
def schoolyear(date):
    if int(date.split("/")[0]) <8 : return date.split("/")[2]
    else: return str(int(date.split("/")[2])+1)
    
    

# Files are hardwired for testing    
# PCG Enrollment
EnrollFile ="C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\StudentEnrollmentPCG.csv"
# Calendar dump
CalendFile ="C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\Calendar.csv"

# Output file for Tableau
Outfile = "C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\TableauFormat\ProcessedEnroll.csv"
Wcsvfile = open(Outfile,'a+b')
wr= csv.writer(Wcsvfile, delimiter=',')

Ecsvfile = open(EnrollFile,'rb')
Ccsvfile = open(CalendFile,'rb')
Ereader = csv.reader(Ecsvfile)
Creader = csv.reader(Ccsvfile)

#Work through every day in the calendar
# except not in the future
Today= time.strftime('%m/%d/%Y')
T_Today = datetime.strptime(Today,'%m/%d/%Y')
print Today,T_Today
for Crow in Creader: 
    cal_date = datetime.strptime(date(Crow[0]),'%m/%d/%Y')
    if cal_date <= T_Today:
        if Crow[1]=='TRUE': # school day
            print "Processing Calendar day:  ", Crow[0]    
            cal_day =  cal_date.strftime("%a")
            next(Ereader)   #skip header row in enrollment file
# Work through every enrollment record for the period selected
            for Erow in Ereader:    #each student
                wrow=[]
                Enrolled = False
                date_start = datetime.strptime(date(Erow[1]),'%m/%d/%Y') 
# entry, nowithdrawal. Is the entry date before the calendar date?
                if Erow[2]=='':
                    if date_start<= cal_date: Enrolled = True        
                else: 
# entry andwithdrawal. Is the calendar date between the entry and withdrawal dates?
                    date_end = datetime.strptime(date(Erow[2]),'%m/%d/%Y')
                    if date_start <= cal_date <= date_end: Enrolled=True   
                if Enrolled:
                    wrow=[Crow[0],Erow[0],'Enrolled', cal_day,schoolyear(Crow[0])]              
                    wr.writerow(wrow)
            Ecsvfile.seek(0) # next calendar date. Start the enrollments at the beginning
            
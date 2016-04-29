#EnrollTableCreate
#Creates a table of lasid, start date, end date for all
# students. Start with the linear enrollment table.
import csv, string, time, sys
from datetime import datetime

    
def EntryRecord():
    if row[3] in ('Y','E'):
        if row[4]=='Active': return True
    return False
    
def WithdrawRecord():
    if row[3]=='W' and (row[4] <>'Active'): return True
    return False
    
def IgnoreRecord():
    if row[3]=='Active':
        if row[4] in ('E','W'): return True
    return False

def getLastEntryIndex():
    allMatches=[x for x,y in enumerate(Grid) if y[0]==row[0]]
    return allMatches[-1] # return the last one

def NewRow():
    Grid.append([row[0],row[1],None])
    return
    
def WriteGrid():
    for x,y in enumerate(Grid):
        wr.writerow(y)
    
Grid=[] # LASID, StartDate, EndDate
# Open the raw file    
EnrollFile ="C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\StudentEnrollment.csv"
Ecsvfile = open(EnrollFile,'rb')
Ereader = csv.reader(Ecsvfile)

Outfile = "C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\TableauFormat\Enrollment.csv"
Wcsvfile = open(Outfile,'a+b')
wr= csv.writer(Wcsvfile, delimiter=',')

#first enrollment date we care about
Start=datetime.strptime("09/01/2004",'%m/%d/%Y')

#Main loop row[0]=LASID, row[1]=Date, row[2] = Description row[3] = Code row[4] = Status
try:
    Count = 0
    sys.stdout.write('Processing .')
    for row in Ereader:
        Count +=1
        if(Count==10000):
            sys.stdout.write('.')
            Count =0
        if datetime.strptime(row[1],'%m/%d/%Y')>=Start:
            if row[0] not in [elem[0] for elem in Grid]:  #elem[0] is the Lasid
                if EntryRecord():
                    #genuinely new record
                    NewRow()
            else:
                LastEntry = getLastEntryIndex()
                LastExitDate = Grid[LastEntry][2]  # last exit date
                if EntryRecord():  # an entry record       
                    if LastExitDate <>  None: NewRow()
                elif WithdrawRecord():
                    if LastExitDate==None: 
                        Grid[LastEntry][2]=row[1]
except: 
    print "encountered end of file"
        
WriteGrid()
            
 
         
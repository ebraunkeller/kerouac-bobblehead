# Process the attendance table for a public viewitems
# join attendance with demographics and
# Retain  the individual student data
# Input files: DistrictAttend.csv created by script appending enrollment and attendance data
#              AllStudents.csv - pulled from X2
# Output file: DistrictView.csv

import pandas as pd
import csv, gc
# map the codes to the definitions:
frl_dict = {"00":'Not',"01":'Free',"02":'Red'}
lep_dict = {"00":'Not',"01":'LEP',"02":'LEP',"03":'LEP'} 

AttFile="C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\TableauFormat\DistrictAttend.csv"
DemFile = "C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\TableauFormat\AllStudents.csv"
OutFile = "C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\TableauFormat\DistrictView.csv"

dfA=pd.read_csv(AttFile,dtype='str')
dfS=pd.read_csv(DemFile,dtype='str')
# remove spaces on the field names
dfS.columns=['LASID','Gender','Race','Ethnicity','SchoolName','SchoolID','Grade','HRTeacher','LimitedEnglish','FRLStatus','SPEDStatus','ENRStatus','FirstName','LastName']
#Join the tables
df = pd.merge(dfA,dfS,left_on='Lasid',right_on='LASID')

# Replace the entries with meaninful values
df.FRLStatus= df.FRLStatus.replace(frl_dict)
df.LimitedEnglish= df.LimitedEnglish.replace(lep_dict)    


df.to_csv(OutFile)


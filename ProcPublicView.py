# Process the attendance table for a public viewitems
# join attendance with demographics and
# aggregate out the individual students

import pandas as pd
import csv
# map the codes to the definitions:
frl_dict = {"00":'Not',"01":'Free',"02":'Red'}
lep_dict = {"00":'Not',"01":'LEP',"02":'LEP',"03":'LEP'} 

AttFile="C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\TableauFormat\DistrictAttend.csv"
DemFile = "C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\TableauFormat\AllStudents.csv"
OutFile = "C:\Users\Elaine\Documents\BKL\Lowell\\2016-2017\TableauFormat\PublicAttend.csv"

dfA=pd.read_csv(AttFile,dtype='str')
dfS=pd.read_csv(DemFile,dtype='str')
# remove spaces on the field names
dfS.columns=['LASID','Gender','Race','Ethnicity','SchoolID','SchoolName','Grade','HRTeacher','PrimaryLanguage','HomeLang','LimitedEnglish','FRLStatus','SPEDStatus']
#Join the tables
df = pd.merge(dfA,dfS,left_on='Lasid',right_on='LASID')

# Replace the entries with meaninful values
df.FRLStatus= df.FRLStatus.replace(frl_dict)
df.LimitedEnglish= df.LimitedEnglish.replace(lep_dict)    

df0=df[['Date','Status','Day','SchoolYear','Gender','Race','Ethnicity','SchoolName','Grade',
       'SchoolID','LimitedEnglish','FRLStatus','SPEDStatus']]

df0.to_csv(OutFile)


#!/bin/bash
clear
echo "Starting now...copyright (c) 2016-2017 BKLSchoolVision"
date
cd /Users/Elaine/Documents/Lowell/TableauFormat
echo "Delete old files"
rm Enrollment.csv
rm ProcessedAttend.csv
rm ProcessedEnroll.csv
rm DistrictAttend.csv
rm PublicAttend.csv
cd /Users/Elaine/Documents/Lowell/kerouac-bobblehead
echo "Create the enrollment table"
python EnrollTableCreate.py
echo "process attendance"
python ProcessAttendance.py
echo "process enrollment"
python ProcessEnrollment.py
echo "combine the enrollment and attendance tables"
cd /Users/Elaine/Documents/Lowell/TableauFormat
cat ProcessedAttend.csv ProcessedEnroll.csv > DistrictAttend.csv
echo "join the attendance with the demographics"
cd /Users/Elaine/Documents/Lowell/kerouac-bobblehead
python ProcPublicView.py
echo "bye for now."
date

cd C:\Users\Elaine\Documents\BKL\Lowell\2016-2017\TableauFormat
del ProcessedAttend.csv
del ProcessedEnroll.csv
del DistrictAttend.csv
cd C:\Users\Elaine\Documents\BKL\Lowell\2016-2017\Scripts
python ProcessAttendance.py
python ProcessEnrollment.py

cd C:\Users\Elaine\Documents\BKL\Lowell\2016-2017\TableauFormat
type ProcessedAttend.csv, ProcessedEnroll.csv > DistrictAttend.csv
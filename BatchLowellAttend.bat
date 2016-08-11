cd C:\Users\Elaine\Documents\BKL\Lowell\2016-2017\TableauFormat
del Enrollment.csv
del ProcessedAttend.csv
del ProcessedEnroll.csv
del DistrictAttend.csv
del PublicAttend.csv
del DistrictView.csv
cd C:\Users\Elaine\Documents\BKL\Lowell\2016-2017\
del NewCalendar.csv

cd C:\Users\Elaine\Documents\BKL\Lowell\2016-2017\Scripts
REM  Args: start_Prev_year  end_prev_year  start_current_year end_current_Year
REM change dates at start of academic year
REM Last year: python CalendarDay.py 08/26/2014 06/23/2015 09/01/2015 06/20/2016
python CalendarDay.py 09/01/2015 06/20/2016 08/30/2016 06/22/2017
python EnrollTableCreate.py
python ProcessAttendance.py
python ProcessEnrollment.py


cd C:\Users\Elaine\Documents\BKL\Lowell\2016-2017\TableauFormat
type ProcessedAttend.csv, ProcessedEnroll.csv > DistrictAttend.csv

cd C:\Users\Elaine\Documents\BKL\Lowell\2016-2017\Scripts
REM python ProcPublicView.py # insufficient memory on my little laptop
python ProcStudentView.py
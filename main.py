from datetime import datetime, date, time
import emoji
from application.salary import Salary
from application.db.people import Employee

s = Salary('Data', 23, 'worker', 1000, 13, 1000 )
print(f'{s.name} has salary {s.get_salary()} on {datetime.now()}', emoji.emojize(':woman_dancing: :man_dancing:'))
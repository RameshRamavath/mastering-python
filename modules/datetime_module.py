import  datetime

# naive dates and times

# pass date as integers - don't mention leading zeros in day's part

dt = datetime.date(2020, 8, 31)  # datetime.date(2020,08 {this is not allowed},31)
print(dt)  # 2020-08-31

tdate = datetime.date.today()  # get current local date
print(tdate)  # 2020-08-31
print(tdate.year)
print(tdate.day)
print(tdate.weekday())   # Monday 0, Sunday 6
print(tdate.isoweekday())  # Monday 1, Sunday 7

"""
 **** Time delta ****
 - useful when we work on history dates
 - date2 = date1 + timedelta
 - timedelta = date1 + date2
"""


tdelta = datetime.timedelta(days=7)
print(tdate + tdelta)  # 2020-09-07 - 7 days from today
print(tdate - tdelta)  # 2020-08-24 - 7 days back from today

bday = datetime.date(1993, 6, 3)
till_bday = tdate - bday
print(till_bday.days)  # 9951 days
print(round(till_bday.days/365,2))

"""
Working at timestamp level - min, sec and milli seconds 

* use datetime.datetime  - pass day and other info
"""

t_time = datetime.datetime(2020, 8, 31, 10, 10, 45, 100000)
print(t_time)  # 2020-08-31 10:10:45.100000
print(t_time.time())  # 10:10:45.100000
print(t_time.year)  # 2020

# use timedelta to add days/hours to datetime

time_delta = datetime.timedelta(days=7)
add_hr = datetime.timedelta(hours=1)

print(t_time + time_delta)  # 2020-09-07 10:10:45.100000
print(t_time + add_hr)  # 2020-08-31 11:10:45.100000

# create timezone aware timestamps - use pytz package for this

import pytz

utc_dt = datetime.datetime(2020, 8, 31, 10, 35, 15, tzinfo=pytz.UTC)
print(utc_dt)  # 2020-08-31 10:35:15+00:00
utc_now = datetime.datetime.now(tz=pytz.UTC)
print(utc_now)  # 2020-08-31 16:58:09.715295+00:00

# timestamp in my zone - Asia/Kolkata

time_kolkata = utc_now.astimezone(tz=pytz.timezone('Asia/Kolkata'))
print(f"UTC time - {utc_now} and Indian time - {time_kolkata}")  # UTC time - 2020-08-31 17:04:16.765354+00:00 and Indian time - 2020-08-31 22:34:16.765354+05:30

# get all the timezone from pytz

# for tz in pytz.all_timezones:
#     print(tz)


"""
How to convert Naive timestamp to timezone aware timestamp
"""

dt_now = datetime.datetime.now()
print("date-time now", dt_now)  # 2020-08-31 22:38:29.943989   - not timezone aware - convert this to EST timezone
dt_asia = dt_now.astimezone(pytz.timezone('Asia/Kolkata'))
print('datetime now after timezone setting -', dt_asia)

# localize timezone
asia_tz = pytz.timezone('Asia/Kolkata')
print('datetime now after localize - ', asia_tz.localize(dt_now))

"""
date-time now 2020-08-31 22:46:36.862118
datetime now after timezone setting - 2020-08-31 22:46:36.862118+05:30
datetime now after localize -  2020-08-31 22:46:36.862118+05:30
"""

# convert timezone aware datetime to string and string to timezone aware datetime

dt_string = dt_asia.strftime('%B %d, %Y')
print('date in string format ::: ', dt_string)  # date in string format :::  August 31, 2020

dt_str = 'August 31, 2020'

dt_datetime = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print('datetime post convert ::: ', dt_datetime) # datetime post convert :::  2020-08-31 00:00:00

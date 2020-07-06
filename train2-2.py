import datetime

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

today = datetime.date.today()
this_year = today.year

last_year = this_year - 1
next_year = this_year + 1

years = [this_year , last_year , next_year]

for year in years:
    if is_leap_year(year):
        print(str(year) + "は閏年")
    else:
        print(str(year) + "は閏年ではない") 
while True:
    sum_days=0
    month_tuple=(31,28,31,30,31,30,31,31,30,31,30,31)
    weekday_tuple=('Sunday','Monday', 'Tuesday', 'Wendesday', 'Thursday', 'Friday', 'Saturday')
    year, month, day=map(int,input('input year month day : ').split(sep=' '))
    if year == 0 and month == 0 and day == 0:
        break
    else:
        pass
    for i in range(1,year):
        if i%4==0 and i%100!=0 or i%400==0:
            sum_days+=366
        else:
            sum_days+=365
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        for j in range(month-1):
            if j == 1:
                sum_days+=29
            else:
                sum_days+=month_tuple[j]
    else:
        for x in range(month-1):
            sum_days+=month_tuple[x]
    sum_days+=day
    number_day=sum_days%7
    print("Day (year({}), month({}), day({})) : week_day ({}), elapsed {} days from Jan01AD01".format(year,month,day,weekday_tuple[number_day],sum_days))
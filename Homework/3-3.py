number_space=0
sum_days=0
count_seven=0
month_tuple=(('January',31),('February',28),('March',31),('April',30),('May',31),('June',30),('July',31),('August',31),('September',30),('October',31),('November',30),('December',31))
year, month, day=map(int,input('input year month day : ').split(sep=' '))
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
            sum_days+=month_tuple[j][1]
else:
    for x in range(month-1):
        sum_days+=month_tuple[x][1]
number_day=sum_days%7
if number_day==6:
    space_num=0
else:
    space_num=number_day+1
print()
print(month_tuple[month-1][0],'of year',year)#o
print('============================')
print(' SUN MON TUE WED THR FRI SAT')
print('----------------------------')
for a in range(space_num):
    print('',end='    ')
    count_seven+=1
for b in range(month_tuple[month-1][1]):
    print('%4d'%(b+1),end='')
    count_seven+=1
    if count_seven == 7:
        count_seven=0
        print()
print('\n============================')
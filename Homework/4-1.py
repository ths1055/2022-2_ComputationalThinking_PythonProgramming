array_date=[]
print('Input 10 dates in (year month day) format : ')
for i in range(10):
    before_tuple=[]
    year,month,day=map(int,input('input year, month, day : ').split(sep=' '))
    before_tuple.append(year);before_tuple.append(month);before_tuple.append(day)
    array_date.append(tuple(before_tuple))
    print('L_dates =',array_date)
print('After input of 10 dates : \n','L_dates =',array_date)
date_min=0
date_init=0
for j in range(len(array_date)):
    for k in range(1+j,len(array_date)):
        if array_date[date_min][0] > array_date[k][0]:
            date_min=k
        elif array_date[date_min][0] == array_date[k][0]:
            if array_date[date_min][1] > array_date[k][1]:
                date_min=k
            elif array_date[date_min][1] == array_date[k][1]:
                if array_date[date_min][2] > array_date[k][2]:
                    date_min=k
    array_date[date_min],array_date[j]=array_date[j],array_date[date_min]
    date_min=date_init+1
    date_init+=1
print('After sorting, L_dates = ',array_date)
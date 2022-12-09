class Date:
    def __init__(self, yr, mn, dy):
        self.setYear(yr)
        self.setMonth(mn)
        self.setDay(dy)
    def __str__(self):
        return '(%4d-%2d-%2d)'%(self.getYear(),self.getMonth(),self.getDay())
    def __lt__(self, other):
        if (self.year, self.month, self.day)<(other.year, other.month, other.day):
            return True
        else:
            return False
    def setYear(self, yr):
        self.year=yr
    def setMonth(self, mn):
        if 1<=mn<12:
            self.month=mn
        else:
            print("Date Setting Error %d %d re setting to default value 1"%(self.getYear(),mn))
            self.month=1
    def isLeapYear(self,yr):
        if ((yr%4==0) and (yr%100!=0)or(yr%400==0)):
            return True
        else:
            return False
    def setDay(self, dy):
        day_list=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        if self.isLeapYear(self.year):
            day_list[2]=29
        if 1<=dy<=day_list[self.month]:
            self.day=dy
        else:
            print("Date Setting Error %d %d %d re setting to default value 1"%(self.year,self.month,dy))
            self.day=1
    def getYear(self):
        return self.year
    def getMonth(self):
        return self.month
    def getDay(self):
        return self.day
    

if __name__ == "__main__":
    dates=[
        Date(2000,9,15),
        Date(1997,2,20),
        Date(2001,5,2),
        Date(2001,5,1),
        Date(1999,3,1)
    ]
    print('dates before sorting : ')
    for d in dates:
        print(d)
    dates.sort()
    print('\ndates after sorting : ')
    for d in dates:
        print(d)
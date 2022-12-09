class Time:
    def __init__(self, hr, mn, sec):
        self.setHour(hr)
        self.setMinute(mn)
        self.setSecond(sec)
    def __str__(self):
        return '(%2d-%2d-%2d)'%(self.getHour(),self.getMinute(),self.getSecond())
    def __lt__(self, other):
        if (self.hour, self.minute, self.second)<(other.hour, other.minute, other.second):
            return True
        else:
            return False
    def setHour(self, hr):
        if 0<=hr<=23:
            self.hour=hr
        else:
            print("Time Setting Error %d re setting to default value 0"%(hr))
            self.hour=0
    def setMinute(self, mn):
        if 0<=mn<=59:
            self.minute=mn
        else:
            print("Time Setting Error %d %d re setting to default value "%(self.getHour(),mn))
            self.minute=0
    def setSecond(self, sec):
        if 0<=sec<=59:
            self.second=sec
        else:
            print("Time Setting Error %d %d %d re setting to default value "%(self.getHour(),self.getMinute, sec))
            self.second=0

    def getHour(self):
        return self.hour
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second
    

if __name__ == "__main__":
    times=[
        Time(23,59,59),
        Time(9,0,5),
        Time(13,30,0),
        Time(3,59,59),
        Time(0,0,0)
    ]
    print('dates before sorting : ')
    for t in times:
        print(t)
    times.sort()
    print('\ndates after sorting : ')
    for t in times:
        print(t)
class Person:
    def __init__(self,name,reg_id,age):
        self.setName(name)
        self.setRegID(reg_id)
        self.setAge(age)
    def getName(self):
        return self.name
    def getRegID(self):
        return self.reg_id
    def getAge(self):
        return self.age
    def setName(self,nm):
        self.name=nm
    def setRegID(self,rg_id):
        self.reg_id=rg_id
    def setAge(self,ag):
        if 0<=ag<=250:
            self.age=ag
        else:
            print('*** Error in setting age (name:%s, age:%d)'%(self.name,ag))
            self.age=0
    def __str__(self):
        return "Person(%s, %d, %d)"%(self.getName(),self.getRegID(),self.getAge())

class Student(Person):
    def __init__(self, name, reg_id, age, st_id, major, gpa):
        Person.__init__(self,name,reg_id,age)
        self.setMajor(major)
        self.setSTID(st_id)
        self.setGPA(gpa)
    def getMajor(self):
        return self.mj
    def getSTID(self):
        return self.stid
    def getGPA(self):
        return self.gpa
    def setMajor(self,major):
        set_majors={"EE","ICE","ME","CE"}
        if major in set_majors:
            self.mj=major
        else:
            print('*** Error in setting major (name:%s, major: %s)'%(self.getName(),major))
            self.mj=None
    def setSTID(self,st_id):
        self.stid=st_id
    def setGPA(self,gpa):
        self.gpa=gpa
    def __lt__(self,other):
        if self.gpa>other.gpa:
            return True
        elif self.stid<other.stid:
            return True
        elif self.age<other.age:
            return True
        else:
            return False
    def __str__(self):
        return "Student(%5s, %6d, %3d, %5d, %4s, %2.1f)"%(self.getName(),self.getRegID(),self.getAge(),self.getSTID(),self.getMajor(),self.getGPA())

def compareStudent(st1,st2,compare):
    if compare == 'st_id':
        if st1.stid<st2.stid:
            return True
        else:
            return False

    if compare == 'name':
        if st1.name<st2.name:
            return True
        else:
            return False
            
    if compare == 'gpa':
        if st1.gpa<st2.gpa:
            return True
        else:
            return False

def sortStudent(L_st,compare):
    for i in range(0,len(L_st)):
        min_index=i
        for j in range(i+1,len(L_st)):
            if compareStudent(L_st[j],L_st[min_index],compare):
                min_index=j
        if min_index != i:
            L_st[i],L_st[min_index]=L_st[min_index],L_st[i]

def printStudent(L_st):
    for s in L_st:
        print(s)

def main():
    students=[
        Student("Kim",990101,21,12345,"EE",4.0),
        Student("Lee",980715,22,11234,"ME",4.2),
        Student("Park",101225,20,10234,"ICE",4.3),
        Student("Hong", 110315, 19, 13123, "CE", 4.1),
        Student("Yoon", 971005, 23, 11321, "ICE", 4.2),
        Student("Wrong", 100000, 23, 15321, "??", 3.2)]
    print('student before sorting : ')
    printStudent(students)

    sortStudent(students,"name")
    print('\nstudents after sorting by name : ')
    printStudent(students)

    sortStudent(students,"st_id")
    print('\nstudents after sorting by student_id : ')
    printStudent(students)

    sortStudent(students,"GPA")
    print('\nstudents after sorting by GPA in decreasing order : ')
    printStudent(students)

if __name__ == "__main__":
    main()
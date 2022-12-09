class Mtrx:
    def __init__(self, name, number_row, number_column, List_data):
        self.name=name
        self.row=number_row
        self.column=number_column
        self.list=[];index_list=0
        for i in range(self.row):
            list_row=[]
            for j in range(self.column):
                list_row.append(List_data[index_list])
                index_list+=1
            self.list.append(list_row)

    def __str__(self):
        result="%s = \n"%(self.name)
        for i in range(self.row):
            for j in range(self.column):
                result+="%8.2f"%(self.list[i][j])
            result+='\n'
        return result

    def __add__(self,other):
        result=[]
        for i in range(self.row):
            for j in range(self.column):
                result.append(self.list[i][j]+other.list[i][j])
        return Mtrx('result',self.row,self.column,result)
        
    def __sub__(self,other):
        result=[]
        for i in range(self.row):

            for j in range(self.column):
                result.append(self.list[i][j]-other.list[i][j])
        return Mtrx('result',self.row,other.column,result)

    def __mul__(self,other):
        result=[]
        for i in range(self.row):#3
            for j in range(other.column):#3
                sum_matrix=0
                for k in range(self.column):#5
                    sum_matrix+=self.list[i][k]*other.list[k][j]
                result.append(sum_matrix)
        return Mtrx('result',self.row,other.column,result)

    def setName(self,name):
        self.name=name

def main():
    LA = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    LB = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
    LC = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
    mA = Mtrx("mA", 3, 5, LA)
    print(mA)

    mB = Mtrx("mB", 3, 5, LB)
    print(mB)

    mC = Mtrx("mC", 5, 3, LC)
    print(mC)
    mD = mA + mB
    mD.setName("mD = mA + mB")
    print(mD)
    mE = mA - mB
    mE.setName("mE = mA - mB")
    print(mE)
    mF = mA * mC
    mF.setName("mF = mA * mC")
    print(mF)

if __name__=='__main__':
    main()
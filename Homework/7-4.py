class Mtrx:
    def __init__(self, name, n_row, n_col, list_data):
        self.name=name
        self.row=n_row
        self.column=n_col
        self.data_list=[]
        list_index=0
        for i in range(self.row):
            list_row=[]
            for j in range(self.column):
                list_row.append(list_data[list_index])
                list_index+=1
            self.data_list.append(list_row)
    
    def __add__(self,other):
        result_list=[]
        for i in range(self.row):
            for j in range(self.column):
                result_list.append(self.data_list[i][j]+other.data_list[i][j])
        return Mtrx('result A',self.row,self.column,result_list)#리스트 열 하나를 통째로 넘겨주기 때문에 수정필요
    
    def __sub__(self,other):
        result_list=[]
        for i in range(self.row):
            for j in range(self.column):
                result_list.append(self.data_list[i][j]-other.data_list[i][j])
        return Mtrx('result B',self.row,self.column,result_list)

    def __mul__(self,other):
        result_list=[]
        sum_matrix=0
        for i in range(self.row):#3
            for j in range(other.column):#3
                sum_matrix=0
                for k in range(self.column):#5
                    sum_matrix+=self.data_list[i][k]*other.data_list[k][j]
                result_list.append(sum_matrix)
        return Mtrx('result C',self.row,other.column,result_list)
    
    def __str__(self):
        result='%s\n'%(self.name)
        for i in range(self.row):
            for j in range(self.column):
                result+="%3d"%(self.data_list[i][j])
            result+='\n'
        return result
    
    def setName(self,new_name):
        self.name=new_name
if __name__ == '__main__':
    LA=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    LB=[1,0,0,0,0,0,1,0,0,0,0,0,1,0,0]
    LC=[0,0,0,1,0,0,0,1,0,0,0,1,0,0,0]
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
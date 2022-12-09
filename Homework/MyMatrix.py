def printMtrx(name,M):
    print('%s ='%(name))
    for i in range(len(M)):
        for j in range(len(M[1])):
            print('%3d'%(M[i][j]),end='')
        print()

def addMtrx(matrix1,matrix2):
    matrix_result=[]
    for i in range(len(matrix1)):
        temp=[]
        for j in range(len(matrix1[1])):
            temp.append(matrix1[i][j]+matrix2[i][j])
        matrix_result.append(temp)
        del temp
    return matrix_result

def subMtrx(matrix1,matrix2):
    matrix_result=[]
    for i in range(len(matrix1)):
        temp=[]
        for j in range(len(matrix1[1])):
            temp.append(matrix1[i][j]-matrix2[i][j])
        matrix_result.append(temp)
        del temp
    return matrix_result

def mulMtrx(matrix1,matrix2):
    matrix_result=[]
    sum_matrix=0
    for i in range(len(matrix1)):#3
        temp=[]
        for j in range(len(matrix2[0])):#3
            sum_matrix=0
            for k in range(len(matrix1[0])):#5
                sum_matrix+=matrix1[i][k]*matrix2[k][j]
            temp.append(sum_matrix)
        matrix_result.append(temp)
        del temp
    return matrix_result

if __name__ == "__main__":
    matrix1=[[1,2,3,4],[5,6,7,8],[9,10,0,1]]
    matrix2=[[1,0,0,0],[0,1,0,0],[0,0,1,1]]
    printMtrx('matrix1',matrix1)
    printMtrx('1+2',addMtrx(matrix1,matrix2))
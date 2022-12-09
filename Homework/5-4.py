def printMtrx(name,M):
    print('%s ='%(name))
    for i in range(len(M)):
        for j in range(len(M[1])):
            print('%3d'%(M[i][j]),end='')
        print()

def mtrxAdd(M1,M2):
    mR=[]#행렬 덧셈은 각각 다른 행렬의 같은 자리 끼리 더함
    for i in range(len(M1)):
        mR_temp=[]
        for j in range(len(M1[1])):
            mR_temp.append(M1[i][j]+M2[i][j])
        mR.append(mR_temp)
        del mR_temp
    return mR

def mtrxSub(M1,M2):
    mR=[]#뺄셈은 각각 다른 행렬의 같은 자리 끼리 뺌
    for i in range(len(M1)):
        mR_temp=[]
        for j in range(len(M1[1])):
            mR_temp.append(M1[i][j]-M2[i][j])
        mR.append(mR_temp)
        del mR_temp
    return mR

def mtrxMul(M1,M2):
    mR=[]
    sum_matrix=0
    for i in range(len(M1)):#3
        mR_temp=[]
        for j in range(len(M2[0])):#3
            sum_matrix=0
            for k in range(len(M1[0])):#5
                sum_matrix+=M1[i][k]*M2[k][j]
            mR_temp.append(sum_matrix)
        mR.append(mR_temp)
        del mR_temp
    return mR

def main():
    A=[[1,2,3,4],[5,6,7,8],[9,10,0,1]]
    B=[[1,0,0,0],[0,1,0,0],[0,0,1,1]]
    C=[[1,0,0],[0,1,0],[0,0,1],[0,0,0]]

    printMtrx('A',A)
    printMtrx('B',B)
    printMtrx('C',C)
    
    after_add_AB=mtrxAdd(A,B)
    printMtrx('A+B',after_add_AB)
    
    after_sub_AB=mtrxSub(A,B)
    printMtrx('A_B',after_sub_AB)

    after_mul_AC=mtrxMul(A,C)
    printMtrx('A*C',after_mul_AC)
    
if __name__ == "__main__":
    main()
import numpy as np

def loadtxt(file_name):
    f=open(file_name,'r')
    data=f.readlines()
    temp=[]
    for i in range(len(data)):
        line=list(map(float,data[i].split()))
        temp.append(line)
    f.close()
    return np.array(temp)

def main():
    A=loadtxt('mat_data_10_2.txt')
    print('A =\n',A)
    A_det=np.linalg.det(A)
    A_inv=np.linalg.inv(A)
    E=np.matmul(A, A_inv)
    print('A_det = ',A_det)
    print('A_inv =\n',A_inv)
    print('E= np.matmul (A, A_inv) =\n',E)

if __name__ == "__main__":
    main()
import numpy as np

A=np.array([[1,5,3,3,7],[3,4,5,6,7],[1,3,5,7,9],[3,1,4,1,5],[5,5,3,3,1]])
B=np.array([105,135,145,74,75])

print('A =\n',A)
print('B =\n',B)
A_inv=np.linalg.inv(A)
A_det=np.linalg.det(A)
print('det_A =\n',A_det)
print('inv_A =\n',A_inv)

X=np.linalg.solve(A,B)
B1=np.matmul(A,X)
X1=np.matmul(A_inv,B)
print('X =\n',X)
print('B1 = A * X =\n',B1)
print('X1 = inv_A * B =\n',X1)
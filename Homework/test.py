import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.integrate import odeint
def sir(x,t,b,c,n):
    s=x[0]
    i=x[1]
    r=x[2]
    dsdt = -b*s*i/n
    didt = b*s*i/n-c*i
    drdt = c*i
    return [dsdt,didt,drdt]
tdata = np.linspace(0,200)
b=0.14
c=0.14285714
n=50000
x0 = [n-1,1,0]
sol = odeint(sir,x0,tdata,args=(b,c,n))

plt.figure(figsize=(8,8))
plt.plot(tdata, sol[:,0],'b', label = 's')
plt.plot(tdata, sol[:,1],'r', label = 'I')
plt.plot(tdata, sol[:,2],'g', label = 'R')
plt.xlabel("days")
plt.ylabel("number of people")
plt.legend()
plt.show()
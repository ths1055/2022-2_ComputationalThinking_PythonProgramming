import numpy as np
import matplotlib.pyplot as plt

def gauss(mu, sigma, X):
    y=(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-1*((X - mu)**2)/(2*sigma**2))
    return y
    

def graph1():
    x=np.linspace(-8,8,100+1)
    y1=gauss(0,0.5,x)
    plt.plot(x,y1,color='red',label='sigma=0.5')
    y2=gauss(0,1,x)
    plt.plot(x,y2,color='blue',label='sigma=0.1')
    y3=gauss(0,2,x)
    plt.plot(x,y3,color='green',label='sigma=0.5')
    plt.title('Normal Distribution Graph 1 - mu = 0.0, sigma = [0.5, 1, 2]')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()

def graph2():
    x=np.linspace(-8,8,100+1)
    y1=gauss(-2.0,1,x)
    plt.plot(x,y1,color='red',label='mu=-2.0')
    y2=gauss(0.0,1,x)
    plt.plot(x,y2,color='blue',label='sigma=0.0')
    y3=gauss(2.0,1,x)
    plt.plot(x,y3,color='green',label='sigma=2.0')
    plt.title('Normal Distribution Graph 2 - mu = [-2.0, 0.0, 2.0], sigma = 1')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    graph1()
    graph2()
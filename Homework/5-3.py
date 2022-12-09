import time
memo=dict()
def dynFibo(n):
    if n in memo:
        return memo[n]
    elif n <=1:
        memo[n]=n
        return n
    else:
        f=dynFibo(n-1)+dynFibo(n-2)
        memo[n]=f
        return f

(start,stop,step)=tuple(map(int,input('input start, stop, step of Fibonacii series : ').split(' ')))
for n in range(start, stop+1,step):
    time1=time.time()
    fibo_n=dynFibo(n)
    time2=time.time()
    elapsed_time=time2-time1
    print('dynFibo({:3d}) = {:25d},took {:10.2f}[micro_sec]'.format(n,fibo_n,elapsed_time))
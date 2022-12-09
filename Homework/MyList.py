import random

def genRandList(L,size):
    for i in range(size):
        L.append(i)
    random.shuffle(L)

def shuffleList(L):
    random.shuffle(L)

def printListSample(L,num_sample,num_line):
    count=0
    for i in range(num_line):
        for j in range(num_sample):
            print('%6d'%(L[count]),end=' ')
            count+=1
        print()
    print('     ......')
    num_printing=num_line*num_sample
    num_len=len(L);num_len-=num_printing
    count=0
    for i in range(num_line):
        for j in range(num_sample):
            print('%6d'%(L[num_len+count]),end=' ')
            count+=1
        print()
    print()

if __name__ == "__main__":
    list_test=[]
    genRandList(list_test,100000)
    printListSample(list_test,3,10)
    shuffleList(list_test)
    printListSample(list_test,3,10)
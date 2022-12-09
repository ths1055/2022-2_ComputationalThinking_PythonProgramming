import time, random

def genBigRandList(n):
    L=[]
    for i in range(0,n):
        L.append(i) 
    random.shuffle(L)
    return L

def printListSample(L,per_line=10,sample_lines=2):
    count=0
    size=len(L)
    for i in range(0,sample_lines):
        s=""
        for j in range(0,per_line):
            if count>=size:
                break
            s+="{0:>8}".format(L[count])
            count+=1
        print(s)
        if count>=size:
            break
    if count < size:
        print('......')
        if count<(size-per_line*sample_lines):
            count=size-per_line*sample_lines
        for i in range(0,sample_lines):
            s=""
            for j in range(0,per_line):
                if count>=size:
                    break
                s+="{0:>8}".format(L[count])
                count+=1
            print(s)
            if count>=size:
                break

def _merge(L_left, L_right):
    L_res=[]
    i,j=0,0
    len_left, len_right = len(L_left), len(L_right)
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]:
            L_res.append(L_left[i])
            i += 1
        else:
            L_res.append(L_right[j])
            j += 1
    while (i < len_left):
        L_res.append(L_left[i])
        i += 1
    while (j < len_right):
        L_res.append(L_right[j])
        j += 1
    return L_res

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid=len(L)//2
        L_left=mergeSort(L[:mid])    
        L_right=mergeSort(L[mid:])
        return _merge(L_left,L_right)

while True:
    print('\nPerformance test of merge sorting algorithm')
    size=int(input('Input size of random list L (0 to quit) ='))
    if size == 0:
        break
    L=genBigRandList(size)
    print('\nBefore merge Sort of L :')
    printListSample(L,10,2)
    time1=time.time()
    sorted_L=mergeSort(L)
    time2=time.time()
    print('After mergeSort of L:')
    printListSample(sorted_L,10,2)
    time_elapsed=time2-time1
    print('Merge sorting took {} sec'.format(time_elapsed))
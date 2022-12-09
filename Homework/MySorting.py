import MyList
def selectionSort(L):
    list_length=len(L)
    for i in range(0,list_length-1):
        index_min=i
        for j in range(i+1,list_length):
            if(L[index_min]>L[j]):
                index_min=j
        if(index_min!=i):
            L[index_min],L[i]=L[i],L[index_min]
def _merge(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    list_lower = _merge(arr[:mid])
    list_higher = _merge(arr[mid:])

    list_merged = []
    l = h = 0
    while l < len(list_lower) and h < len(list_higher):
        if list_lower[l] < list_higher[h]:
            list_merged.append(list_lower[l])
            l += 1
        else:
            list_merged.append(list_higher[h])
            h += 1
    list_merged += list_lower[l:]
    list_merged += list_higher[h:]
    return list_merged

def mergeSort(L):
    if len(L) < 2:
        return L[:]
    else:
        L_result = _merge(L)
    for i in range(len(L)):
        L[i] = L_result[i]

if __name__ == "__main__":
    test=[]
    MyList.genRandList(test,10000)
    MyList.printListSample(test,3,10)
    selectionSort(test)
    MyList.printListSample(test,3,10)
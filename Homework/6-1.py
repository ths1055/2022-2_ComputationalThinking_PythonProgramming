import sys
myPyModules_dir="C:/MyPyPackage/myPyModules"
sys.path.append(myPyModules_dir)

import MyList, MySorting

L=[]
n=100

MyList.genRandList(L,n)
print('Before Sorting :')
MyList.printListSample(L,10,3)

MySorting.selectionSort(L)

print('\nAfter Sorting :')
MyList.printListSample(L,10,3)

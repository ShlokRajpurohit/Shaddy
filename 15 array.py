from array import *
arr=array('i',[5,67,3,8,29,11])
newArr=array(arr.typecode,(a**2 for a in arr))
for i in newArr:
    print(i)
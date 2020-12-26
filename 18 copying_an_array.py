from numpy import *

arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,10])
arr3=arr1+arr2
print(arr3)

print(sin(arr1))#any trignometric ratios
print(log(arr1))#finding log values of any number
print(sqrt(arr1))#square root of any number
print(min(arr1))#can find the minimum and the maximum values
print(sort(arr1))#can sort elements if not in order
print(concatenate([arr1,arr2]))#combining 2 or more arrays

#Copping an array
arr4=arr1.view()#this creates 2 different arrays with 2 different adresses
arr5=arr1.copy()#this is same as .view but if we change value of arr1 it will not affect arr5
arr1[1]=7

print(arr1)
print(arr4)
print(arr5)
from numpy import *

arr1 = array([
                [1,2,3,6,2,9],
                [4,5,6,7,5,3]
            ])

arr2=arr1.flatten()#to convert to 1D array
arr3=arr2.reshape(2,2,3)#to convert to 3D array
arr4=array([
                [1,2,3,6],
                [4,5,6,7]
            ])
m1=matrix(arr4)#to convert into a matrix
m4=matrix('1,2,3; 4,5,6; 7,8,9')
m2=matrix('1,4,8; 5,7,3; 9,0,5')

m3=m2+m4#to add two metrices

print(arr1)
print()#printing a blank line
print(arr2)
print()#printing a blank line
print(arr3)
print()#printing a blank line
print(arr4)
print()#printing a blank line
print(m1)
print(diagonal(m1))#to get the diagonal values
print(m1.min())#to print min and max values in a matrice
print(m3)
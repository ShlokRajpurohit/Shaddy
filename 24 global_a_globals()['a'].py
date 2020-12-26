'''GLOBLAL KEYWORD'''

a=10#this is a global variable as it is outside the function
def something():
    a=15#this is a local variable as it is inside the function
    b=8#we can print 'b' only inside this function i.e.; the scope of 'b' is only inside
    print('inside function',a)
#we can also use a global variable inside a function
print('outside function',a)
something()
print()
def change():
    global a #we are telling python that we want to use the global variable and not the local one
    a=20
    print('in func',a)
    a=9
change()
print('outside',a)#here the global variable is also 20
print()
#when we want the global and the local variable in the same function
one=1
print(id(one))
def var():
    one=2
    x=globals()['one']#this is used to access all the global variables
    print(id(x))
    print(x)
    print('in func',one)
    globals()['one']=3#changing the value of 'one'
var()
print('ouside',one)
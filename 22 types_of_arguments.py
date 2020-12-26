def person(name,age):
    print(name)
    print(age-5)
#position argument
print('shlok',15)#position is dependent
print()

#keyword argument
person(age=15,name='shlok')#can give the keyword to assign a variable
print()

#default argument
def account(name1,age1=18):
    print(name1)
    print(age1)
account('shlok',28)#if we enter everything its well and good
print()
account('shlok')#if we do not pass the age it should be by default 18
print()

#variable length argument
def sum(a,b):
    c=a+b
    print(c)
sum(5,6)#in this we can only pass 2 numbers
print()
def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
sum(5,6,34,78)#in this we can have multiple values to add!
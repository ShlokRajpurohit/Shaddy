# if Elif Else statement
x=3
r=x%2
if r==0:
    print('Even')
    if x>5:
        print('Greater')
    else:
        print('Smaller')
else:
    print('Odd')
    if x>5:
        print('Greater')
    else:
        print('Smaller')
print('Bye')

print()

x=int(input('Enter a number '))
if x==1:
    print('One')
elif x==2:
    print('Two')
elif x==3:
    print('Three')
elif x==4:
    print('Four')
else:
    print('Wrong Input!')
print('Bye')
def greet():
    print('Hola')
greet()

def add_sub(x,y):
    a=x+y
    s=x-y
    return a,s
print(add_sub(int(input('Enter a value:- ')),int(input('Enter another value:- '))))

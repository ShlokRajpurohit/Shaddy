def fact(n):
    if(n==0):
        return 1

    return n*fact(n-1)

result=fact(int(input('Hey user enter a value that you find a factorial of:- ')))
print(result)
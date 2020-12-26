def div(a,b):
    print(a/b)

def smart_div(func):#This is a decorator used to modify an existing code

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div=smart_div(div)#connection b/w div and smart div

div(2,4)
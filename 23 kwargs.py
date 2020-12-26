'''KEYWORD VARIABLE LENGTH ARGUMENTS(**kwargs)'''

def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person('shlok',age=15,city='Delhi',mob=1234567890)
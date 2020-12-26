import sys
sys.setrecursionlimit(999999999)
print(sys.getrecursionlimit())
i=0

def greet():
    global i
    i+=1
    print('Hello',i)
    greet()
greet()
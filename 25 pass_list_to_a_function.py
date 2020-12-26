'''LIST IN A FUNCTION'''
#return the number of even values and the number of odd numbers

def count():
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst=[1,23,55,68,34]
even,odd=count()
print('Even:{} and Odd:{}'.format(even,odd))

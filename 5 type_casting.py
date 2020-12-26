#one data type into another
#Data types, int, floats, string, booleans

percentage=98.89
plainData=int(percentage) # 90.89-> 90
print(plainData)
print(type(str(percentage))) #90.89-> str

#type function(tells the type)

print(type(67))
print(type(98.89))
print(type('Hello'))
print(type(True))

#converting to Booleans is a bit different(and difficult😁)
a=5
print(bool(a))#any non zero number is True, and zero is False
data=[4]#filled data types True, unfilled data types fales
print(bool(data))
data2="x"
print(bool(data2))
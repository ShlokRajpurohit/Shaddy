#Break statement
av=3
x=int(input('How many Candies you want? '))

i=1
while i<=x:
    if i>av:
        print('Sorry, we are out of stock!☹')
        break
    print('🍬')
    i+=1
print('Thanks for shopping with us. 😊')

#Continue statement
for e in range(1,101):
    if e%3==0 or e%5==0:
        continue
    print(e)
print('END!')

#Pass statement
for a in range(1,101):
    if(a%2!=0):
        pass
    else:
        print(a)
print('Bye')
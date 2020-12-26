nums=[34,67,40,56,7,66]

for num in nums:
    if num%5==0:
        print(num)
        break#break is neccessary
else:
        print('No values divisible by 5')
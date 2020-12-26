x=74
for i in range(2,x):
    if x%i==0:
        print('Composite')
        break
else:
    print('Prime')
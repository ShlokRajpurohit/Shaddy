

nums=[2,5,7,4,9,2,5,6]
#filter
evens=list(filter(lambda n:n%2==0,nums))
#map
doubles=list(map(lambda d:d*2,evens))
from functools import reduce
#reduce
sum=reduce(lambda a,b:a+b,doubles)

print(evens)
print(doubles)
print(sum)
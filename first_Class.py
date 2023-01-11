nums=[1,6,7,3,8]

min_n=99999
max_n=0

for i in nums:
    if min_n>i:
        min_n=i
    
    if max_n<i:
        max_n=i


print(max_n,min_n)
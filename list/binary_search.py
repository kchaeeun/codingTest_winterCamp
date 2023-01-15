def solution(L,x):
    first=0
    last=len(L)-1


    while first<=last:
        middle=(first+last)//2
        if x == L[middle]:
            return middle

        elif x<L[middle]:
                last -=1
        else:
                first+=1

    return -1

lst=[1,2,4]

print(solution(lst,5))
  


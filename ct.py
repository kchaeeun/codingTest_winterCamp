def solution(L, x):
    answer = 0
    idx=int((len(L)-1)/2)
    #for idx in range(len(L)):
    #   if L[idx]==x:
    #       answer=idx
    if x not in L:
         answer=-1  
    else:
        def s(i1,i2):
            idx=int((i1+i2)/2)
            if x>L[idx]:
                L=L[idx+1:len(L)]
                s(idx+1,len(L)-1)
                solution(L,x)
                
            elif x<L[idx]:
                L=L[0:idx]
                s(0,idx-1)
                solution(L,x)


            else:
                answer=idx

            
    return answer

lst=[1,2,3,4,5,7]
print(solution(lst,4))
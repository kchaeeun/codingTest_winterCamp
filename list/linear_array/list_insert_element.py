def solution(L, x):
    for idx in range(0,len(L)):
        if L[idx] >= x:
            L.insert(idx,x)
            break
        
    if L[len(L)-1]<x:
        L.insert(len(L),x)
            
    return L
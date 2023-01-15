def solution(L,x):
    first=0
    last=len(L)-1

    while first<=last:
        middle=(first+last)//2
        if x == L[middle]:
            return middle

        elif x<L[middle]:
            last= middle -1
        else:
            first = middle+1

    return -1
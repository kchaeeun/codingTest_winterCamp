def solution(L, x, l, u):
    #if x not in L:                      #재귀함수를 돌리다보면 맨 앞의 인덱스 l의 값이 u를 역전할 수 있음
    if l > u :                           #원하는 x가 없을 때 조건 설정은 '효율성' 면에서 2줄보다 더 좋다. *중요
        return -1                        #그 경우에는 선형 배열을 돌리지 않아도(O(n)) x값이 리스트에 없음을 한번에 알 수 있다.(O(1))
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)

    else:
        return solution(L, x, mid+1, u)

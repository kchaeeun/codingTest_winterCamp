#left값과 right값 모두 함수의 인수가 되게 만들기
def found_middle(lst, num, left,right):
    if left>right: #리스트에 존재하지 않는 num
        return -1
    
    middle=int((left+right)/2)
    if num == lst[middle]:
        return middle
    elif num > lst[middle]:
        return   found_middle(lst,num,middle+1,right)
    else:
        return   found_middle(lst,num,left,middle-1)

def solution(L, x):
    answer = found_middle(L,x,0,len(L)-1)
    return answer
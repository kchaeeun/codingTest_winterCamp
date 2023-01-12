def solution(n, lost, reserve):
    lst = [1]*(n+2)             #값이 1로 채워진 리스트 만들기, n+2로 하여 양끝에 방어벽을 두고 for문을 돌림
    for i in reserve:
        lst[i]+=1
    for i in lost:
        lst[i]-=1
    for i in range(1,len(lst)-1):
        if lst[i-1]==0 and lst[i]==2: #뒤 친구에게 도움 받기
            lst[i-1:i+1]=[1,1]
        elif lst[i]==2 and lst[i+1]==0: #앞 친구에게 도움 받기
            lst[i:i+2]=[1,1]

    #len([x for x in lst[1:len(lst)-1] if x!=0])
    return len([x for x in lst[1:-1] if x>0]) #return값 : 리스트 값이 1이여서 체육복이 있는 학생 수

#print(solution(5,[2,4],[3]))
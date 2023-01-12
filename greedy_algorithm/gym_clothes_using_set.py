#n의 수(인원 수)가 많은데 여벌의 체육복을 가져온 학생 수가 적을 때 더 효율적인 방법
def solution(n,lost,reserve):
    s=set(lost)&set(reserve) #교집합 : 체육복이 1개인 집단
    l=set(lost) -s           #아예 체육복이 없는 집단 : 0개 가지고 있는 집단
    r=set(reserve) - s       #체육복을 잃어버리지 않아 2개 가지고 있는 집단
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1) 
        elif x+1 in l:
            l.remove(x+1)

    return n - len(l)   #l집합에 남아 있는 번호는 체육복을 나눠 받지 못한 사람의 번호

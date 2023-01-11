def solution(participant, completion):
    d={}
    for x in participant:
        d[x]=d.get(x,0)+1 #값이 '없으면' 반환할 값을 지정한다.
    for x in completion:
        d[x]-=1
    dnc=[key for key,value in d.items() if value!=0 ] #딕셔너리 중에서 value값이 0이 아닌 key값을 리스트에 저장해라
    answer=dnc[0]
    return answer
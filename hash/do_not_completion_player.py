def solution(participant, completion):
    participant.sort()
    print(participant)
    completion.sort()
    print(completion)
    
    for x in range(len(completion)):
        if completion[x]!=participant[x]:
            return participant[x]
    return participant[len(participant)-1] #정렬로 인해 루프를 돌지조차 못하는 인덱스 값이 발생, 그렇게 되면 그 인덱스 값이 남은 값

p=	["leo", "kiki", "eden"]
c=["eden", "kiki"]

print(solution(p,c))
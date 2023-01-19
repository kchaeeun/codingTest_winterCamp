def solution(x):
    if x == 0:
        answer = x
    elif x == 1:
        answer = x + solution(x-1)
    else:
        answer = solution(x-1)+solution(x-2)
    
    return answer

print(solution(6))

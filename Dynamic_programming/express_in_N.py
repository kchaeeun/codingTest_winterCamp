def solution(N,number):
    s=[set() for _ in range(8)]                 #set은 중복되는 숫자를 제거함
    for i,x in enumerate(s, start=1):           #i는 1부터 시작(x는 인덱스 0부터 시작하기 위해 인덱스 start값을 정해줌)
        x.add(int(str(N)*i))

    for i in range(len(s)):                     #N와 number가 같은 경우 1개만 사용하는 경우도 포함해야함(0~len(s)-1)
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)           #중복 수가 나와도 set덕분에 사라져서 데이터량이 적음
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)    #분모가 0인 경우는 나눗셈 불가, 나머지는 무시 (몫 구하는 연산 사)
        
        if number in s[i]:
            answer =i+1                         #i(인덱스)값이 0부터 시작하고 있기 때
            break

    else:                                       #for문 속 break가 발생하지 않을 때의 경우(number가 s안에 없는 경우)
        answer=-1                               #numbers를 만드는 N의 개수가 8개보다 큰 경우
             

    return answer

#print(solution(4,4))
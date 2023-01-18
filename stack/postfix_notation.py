#후위표기법
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):                                #후의표기법은 사칙연산 부호만 스택에 저장시킨다.
    opStack = ArrayStack()
    answer=''
    for c in S :
        if c not in '(*+/-)':
            answer+=c
        else :
            if c == '(':
                opStack.push(c)
            elif c == ')' :
                while opStack.peek()!='(':                                   #S식에 소괄호를 사용하지 않는 경우도 존재한다.
                    answer+=opStack.pop()
                opStack.pop()                                                #answer에 저장은 안하지만 '('도 삭제해줄 필요o
            else:
                if opStack.isEmpty():
                    opStack.push(c)
                else:
                    while not opStack.isEmpty():
                        if prec[c] <= prec[opStack.peek()] :                #[-1]을 사용하기 보다 peek를 사용해서 데이터를 반환해주는 편이 낫다.
                            answer+=opStack.pop()                                    #while문에 의해(stack이 빌때까지)두번째로 밑에 있던 것까지 사라져준다.
                        else:break
                    opStack.push(c)
                    #print(opStack.peek())
                                        

    while not opStack.isEmpty():                                             #소괄호 밖에 있는 사칙연산을 스택에서 꺼내준다.
        answer += opStack.pop()
    
    return answer

s='A+B/C-L'
print(solution(s))
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):                 #현재 스택에 있는 데이터 원소의 수
        return len(self.data)

    def isEmpty(self):              #스택이 비어 있는지 판단
        return self.size() == 0

    def push(self, item):           #추가
        self.data.append(item)

    def pop(self):                  #가장 마지막에 저장된 데이터 제거
        return self.data.pop()

    def peek(self):                 # =                   데이터 참조 반환
        return self.data[-1]

#수식의 괄호가 올바르게 여닫혀 있는지를 판단하는 함수 solution()#
def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)               #시작 괄호면 스택에 push를 해준다
        elif c in match:            #끝 괄호인데
            if S.isEmpty():         #만약 스택이 비어 있으면 올바르지 않은 수식
                return False
            else:                   #아니라면 pop를 해줘 계속 t에 저장한다
                t = S.pop() 
                if t != match[c]:   #마지막으로 pop한, 즉 첫번째로 넣은 시작괄호가 match의 value에 없다면 올바르지 않은 수식이다.
                    return False

    return  S.isEmpty()             #스택을 끝까지 pop을 해서 스택이 비어 있어야 올바른 수식이다.#
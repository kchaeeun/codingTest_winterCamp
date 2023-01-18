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

#문자열 속 각각의 피연산자와 연산자를 구분하는 함수
#사칙연산 앞뒤의 피연산자가 몇자리수인지 구분
#exprStr -> 중위표현 수식
def splitTokens(exprStr):
    tokens = []
    val = 0                             #각 자리 숫자를 담은 변수
    valProcessing = False               #변수 프로세스 false로 초기화
    for c in exprStr:
        if c == ' ':                    #빈칸이 들어 있으면 패스, cotinue
            continue
        if c in '0123456789':           #숫자를 10진수로 변환
            val = val * 10 + int(c)
            valProcessing = True        #숫자 프로세스를 거쳤음을 의미
        else:   
            if valProcessing:
                tokens.append(val)      #숫자 프로세스를 겪었으면
                val = 0                 #다른 피연산자가 나왔을때를 위해 val을 0으로 초기화
            valProcessing = False       #10진수가 아니므로 False로 처리(위에와 동일한 조건)
            tokens.append(c)
    if valProcessing:                   #변수프로세스 확인 후 변수 처리
        tokens.append(val)
    print(tokens)
    return tokens


def infixToPostfix(tokenList):
    postfixList = []
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    for c in tokenList:
        if c == '(':
            opStack.push(c)
        elif c == ')':
            while opStack.peek() != '(':
                t=opStack.pop()
                postfixList.append(t)
            opStack.pop()
        elif c in prec:
            if opStack.isEmpty():
                opStack.push(c)
            else:
                while not opStack.isEmpty():
                    if prec[c] <= prec[opStack.peek()]:
                        t= opStack.pop()
                        postfixList.append(t)
                    else: break
                opStack.push(c)
        else:
            postfixList.append(c)
                
    while not opStack.isEmpty():
        t=opStack.pop()
        postfixList.append(t)
    print(postfixList)
    return postfixList


def postfixEval(tokenList):                 #후위표기법을 계산할 때도 스택을 사용한다. 
    stack = ArrayStack()                    #이때, 스택에는 중위->후위 때와 반대로 연산자가 push된다.

    for token in tokenList:
        if type(token) is int:
            stack.push(token)
        
        else:
            b,a= stack.pop(), stack.pop()   #각각의 변수에 저장
            if token == '+':
                stack.push(a+b)
            elif token == '-':
                stack.push(a-b)
            elif token == '*':
                stack.push(a*b)
            else:
                stack.push(a/b)

    return stack.pop()
            
def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


s='3*5/(2-1)'
print(solution(s))
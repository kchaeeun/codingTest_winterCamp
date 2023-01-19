#원형 큐
#정해진 개수의 저장공간을 사용
#큐가 가득차면 더 이상 언소를 넣을 수 없음
class CircularQueue:

    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1


    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
        self.rear = (self.rear+1) % self.maxCount   #원형 큐를 끝까지 돌고도 재사용해야되기 때문에 나머지값을 구하는 연산을 사용한다.
                                                    #self.rear+1이 1이어도, 5여도 둘의 값은 인덱스 1로 동일
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = (self.front+1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front+1) % self.maxCount]      #self.front가 -1일때 -> 0으로 만들어주기 위함


def solution(x):
    return 0
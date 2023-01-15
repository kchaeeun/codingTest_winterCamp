class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:           #self.tail 일때
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:                      #노드의 인덱스(pos)는 0이 아닌 '1'부터 시작
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):       #삽입할 때는 prev,next,newnode를 사용
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:     
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):                   #삭제할 때는 prev,next,curr(현재 위치)를 사용
        curr = prev.next                        #삭제 시작 전에 해야할 일 : curr를 정의하기
        
        prev.next = curr.next                   #next = curr.next#
        curr.next.prev = prev                   #next값은 모르기 때문에 다르게 써줘야함
                                                #prev는 인자로 주어졌기 때문에 curr.으로 사용할 필요x
        self.nodeCount -=1
        
        return curr.data
        


    def popBefore(self, next):
        curr = next.prev
        
        curr.prev.next = next                   #prev = curr.prev#
        next.prev = curr.prev
        self.nodeCount -= 1

        return curr.data
    
    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:  
            raise IndexError
            
        else:
            prev = self.getAt(pos-1)
            
            return self.popAfter(prev)                  #※함수 사용할 때는 꼭 함수명 앞에 self.를 해줘야 한다.


def solution(x):
    return 0
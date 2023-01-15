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


    def concat(self, L):                        #L은 병합될 연결 리스트
        self.tail.prev.next = L.head.next       #한쪽 노드가 비어 있어도 head, tail은 존재함으로 나눌 필요 x
        L.head.next.prev = self.tail.prev       #주의 : =의 앞 뒤 순서 헷갈릴 수 있음("왼쪽이 새롭게 생길 친구= new!")
                                                #두 줄이 바뀌어도 영향 X
        self.tail = L.tail                      #L이 self 자체로 병합되어지기 때문에 L의 tail이 즉, self의 tail이 된다.
        
        self.nodeCount += L.nodeCount
            
        return True


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

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
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


def solution(x):
    return 0
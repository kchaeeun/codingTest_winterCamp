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


    def insertBefore(self, next, newNode):      #next의 위치는 알고 있음
        prev = next.prev                        #next를 가지고 prev값 구하기 (newNode 추가되기 전)
        newNode.next = next                     #1. newNode의 연결선 연결
        newNode.prev = prev
        prev.next = newNode                     #2. newNode의 직접적인 노드 연결
        next.prev = newNode
        self.nodeCount += 1
        
        return True

def solution(x):
    return 0
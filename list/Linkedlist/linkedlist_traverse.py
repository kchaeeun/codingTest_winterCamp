class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        if self.nodeCount == 0 :        #노드가 비어 있다면
            return []
        
        curr = self.head                #현 위치는 head(맨앞)
        item = []                       
        
        while curr != None :            
            item.append(curr.data)
            curr = curr.next            #다음 노드로 현재 위치 이동
        
        return item

# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0
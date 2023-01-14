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

        i = 1                   #위치는 1 인덱스부터 시작
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        #※사용자 정의 함수를 사용할 때는 () 인자에 self를 작성하는 대신 self.(포인트)를 사용해준다!
        del_curr = self.getAt(pos)                  #삭제할 노드의 위치
        
        if pos < 1 or pos > self.nodeCount:         #범위를 벗어나는 경우
            raise IndexError
        
        if pos == 1:                                #첫번째 노드 삭제시
            if self.nodeCount == 1:                 #노드의 개수가 한개인 경우
                self.head = None
                self.tail = None
                self.nodeCount = 0
            else:                                   #노드의 개수가 다수인 경우
                self.head = self.head.next
                self.nodeCount -= 1
                
        
        else:                                       #중간 노드 삭제시 and 마지막 노드 삭제 시
            prev = self.getAt(pos-1)                #삭제할 노드의 이전 pos
            prev.next = del_curr.next
            if pos == self.nodeCount :              #마지막 노드 삭제 시
                prev.next = None                    #
                self.tail = prev                    #삭제 노드 이전의 노드가 tail이 됨
            self.nodeCount -= 1
            
        return del_curr.data
            
    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0
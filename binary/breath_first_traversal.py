#<넓이 우선 순회>
#수준이 낮은 노드를 우선으로 방문
class ArrayQueue:                       #배열 큐를 사용

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r                           #레벨 0인 루트 노드


    def bft(self):                              #맨위 트리부터 진행
        traversal, que = [], ArrayQueue()
        if self.root:                           
            que.enqueue(self.root)             
            
        while not que.isEmpty():
            node = que.dequeue()                #삭제된 값은 아직 data값이 아님(class Node확인)
            traversal.append(node.data)         #.data를 붙여줘야 노드 값을 알 수 있음(+순회값 traversal에 저장 중)
            
            if node.left:                       #자식 노드들 다시 que에 저장해 while문이 돌아갈 수 있음(자식노드가 없는 노드에 다다르는 순간 진행x->empty)
                que.enqueue(node.left)
            if node.right:
                que.enqueue(node.right)
        
        return traversal


def solution(x):
    return 0

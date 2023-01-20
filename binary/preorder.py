#전위순회 연산 구현
class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):                          #중위순회
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def preorder(self):                         #inorder와 비슷한 구조                 
        traversal = []
        traversal.append(self.data)             #전위순회는 루트노드를 먼저 거침
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def preorder(self):
         if self.root:
            return self.root.preorder()
         else:                                  #else절 tab 오류
            return []

        
def solution(x):
    return 0
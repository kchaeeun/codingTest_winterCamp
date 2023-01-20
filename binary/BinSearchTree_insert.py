class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):     
        if key < self.key: 
            if self.left != None:                   #왼쪽 자식노드가 있다면
                self.left.insert(key,data)          #key값이 있는 data가 비어 있는 노드에 원하는 data를 저장                    
            else:
                self.left = Node(key,data)          #비어 있다면 Node를 직접 생성해준다.
                
        elif key > self.key:
            if self.right != None:
                self.right.insert(key,data)
            else:
                self.right = Node(key,data)
        
        else :                                      #지금 삽입할 key와 기존의 키값 self.key이 같으면 key값의 오류
            raise KeyError
        return True


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0
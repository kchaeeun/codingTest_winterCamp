class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):                                         #노드 개수
        l = self.left.size() if self.left else 0            #재귀 사용
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        l = self.left.depth() if self.left else 0            #size 함수와 동일하게 재귀알고리즘으로 size를 depth로 바꾸기만 하면 완료
        r = self.right.depth() if self.right else 0
        
        return max(l,r) + 1                                  #둘 중에서 더 큰 것이 depth가 됨 (+1해준 이유는 루트 노드까지 포함시키기 위함)      


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0


    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0


def solution(x):
    return 0
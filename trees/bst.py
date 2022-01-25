class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.display = []

    def insertRoot(self, value):
        if not self.root:
            self.root = Node(value)

    def insert(self, value):
        return self._insert(self.root, value)

    def _insert(self, curNode, value):
        if not self.root:
            self.root = Node(value)

        elif value > curNode.value:
            if curNode.right is None:
                curNode.right = Node(value)
                return
            else:
                return self._insert(curNode.right, value)

        elif value < curNode.value:
            if curNode.left is None:
                curNode.left.value = Node(value)
                return
            else:
                return self._insert(curNode.left, value)

        else:
            return

    def inorder(self):
        from collections import deque
        q = deque()
        curNode = self.root
        q.append(curNode)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                self.display.append(node.value)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return self.display


#root = [1,2,3,4,'null',5,6,null,null,7]
B = BST()

for i in range(1, 8):
    B.insert(i)
print(B.inorder())

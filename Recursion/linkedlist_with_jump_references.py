class Node:
    def __init__(self, val, next=None, jump = None):
        self.val = val
        self.next = next
        self.jump = jump
    def __str__(self):
        arr = []
        root = self
        while root:
            arr.append(root.val)
            root = root.next
        return str(arr)


def recursive_jump_order(root):
    order = 0
    head = root
    def helper(root, order):
        if root is None or root.val != -1:
            return
        root.val = order
        order += 1
        helper(root.jump, order)
        order += 1
        helper(root.next, order)

    helper(head, order)
    return head

def iterative_jump_order(root):
    stack = []
    stack.append(root)
    order = 0
    head = root
    while len(stack)>0:
        node = stack.pop()
        if node is not None and node.val == -1:
            node.val = order
            order += 1
            stack.append(node.next)
            stack.append(node.jump)
    return head
def initialize_linked_list():
    a = Node(-1)
    b = Node(-1)
    c =  Node(-1)
    d =  Node(-1)
    e = Node(-1)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = None

    a.jump = b
    b.jump = d
    c.jump = a
    d.jump = c
    e.jump = d

    return a

def main():
    root = initialize_linked_list()
    root = recursive_jump_order(root)
    print(root)
    
    root = initialize_linked_list()
    root = iterative_jump_order(root)
    print(root)

main()
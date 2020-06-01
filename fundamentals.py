class Node:

    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class fundamentals:
    def __init__(self):
        self.head = None

    def addFront(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # remove the nth node from the linked list
    def remove(self, n):
        cur, follower = self.head, self.head
        step = 0

        while cur:
            if step > n:
                follower = follower.next
            cur = cur.next
            step += 1

        if step == n:
            return self.head.next
        else:
            follower.next = follower.next.next

        return self.head

    # print all items in the linked list //  all methods have access to self.head
    def printall(self):
        cur = self.head

        while cur:
            print(cur.item)
            cur = cur.next

    # check if the linked list is a palindrome
    def isPalindrome(self):
        cur = self.head
        stack = []
        lenn = 0

        while cur:
            cur = cur.next
            lenn += 1

        curr = self.head
        half = 0
        while half < lenn // 2:
            stack.append(curr.item)
            print(curr.item)
            curr = curr.next
            half += 1

        if lenn % 2 != 0: curr = curr.next

        while curr:
            if curr.item != stack.pop(): return False
            curr = curr.next
        return True

    # is the linked list a palindrome
    def evalRPN(self, s):

        stack = []

        for i in s:
            if i in "+ - * /":
                x = int(stack.pop())
                y = int(stack.pop())
                if i == "+":
                    z = x + y
                elif i == "-":
                    z = y - x
                elif i == "*":
                    z = y * x
                else:
                    z = y / x
                stack.append(z)

            else:
                stack.append(int(i))
        return int(stack.pop())


# thy hallowed main method
if __name__ == '__main__':
    ll = fundamentals()
    ll.addFront(1)
    ll.addFront(3)
    ll.addFront(2)
    ll.addFront(1)
    ll.printall()
    print(ll.isPalindrome())
    print(ll.evalRPN("21+3*"))

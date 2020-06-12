# Design and implement a data structure for Least Recently Used (LRU) cache.

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


# Doubly Linked List, helper class
# all methods have time 0(1) except for __str__()
# space is 0(N)
class LinkedList:

    def __init__(self):
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    # adds the provided node to the front of the linked list
    def add_front(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    # removes the last linked list
    def remove_last(self) -> int:
        key = self.tail.prev.key
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return key

    # removes the given node and adds it to the front
    def remove(self, node):
        val = node
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_front(val)

    # string representation of the current node
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur.next:
            out += str(cur.key)
            cur = cur.next

        return out


# Main LRUCache class
# space 0(N)
# all operations are 0(1)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.linked = LinkedList()
        self.size = 0

    # get the requested key if it is in the LRUCache and
    # then add it to the front in the linkedlist
    def get(self, key: int) -> int:

        if key in self.hashmap:
            val = self.hashmap[key]
            self.linked.remove(self.hashmap[key])
            return val.val

        return -1

    # put the key, value pair in the LRUCache(linked list + hash map) checking
    # if it was already there, and if the hashmap is full
    def put(self, key: int, value: int) -> None:

        if self.size == self.capacity:
            rem = self.linked.remove_last()
            del self.hashmap[rem]
            self.size -= 1

        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.linked.remove(node)
            return

        node = Node(key, value)
        self.linked.add_front(node)
        self.hashmap.update({key: node})
        self.size += 1

    # string representation of the hashmap
    def __str__(self):

        out = ""
        for k in self.hashmap:
            out += str(k)
        return out

#["LRUCache","put","put","get","put","put","get"]
#[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2, 1)
obj.put(2, 662)
sol = obj.linked
print("state of linked list:", sol.__str__())
print("state of hash map:", obj.__str__())
print("first get: ", obj.get(2))
obj.put(1, 1)
obj.put(4, 1)
print("state of linked list:", sol.__str__())
print("state of hash map:", obj.__str__())
print("second get: ", obj.get(4))

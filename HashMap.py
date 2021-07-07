class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        self.capacity = 499
        self.HashMap = [Node("dummy", "dummy") for i in range(self.capacity)]

    def Hash(self, key):
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self.Hash(key)
        cur = self.HashMap[index]
        if not cur.next:
            cur.next = Node(key, value)
            return

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Node(key, value)

    def get(self, key: int) -> int:

        index = self.Hash(key)
        cur = self.HashMap[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self.Hash(key)
        cur = self.HashMap[index]
        while cur:
            if cur.next and cur.next.key == key:
                cur.next = cur.next.next
            cur = cur.next


'''        
    def __str__(self):
        out = ""
        for idx in range(len(self.HashMap)):
            cur = self.HashMap[idx].next
            while(cur):
                out += str(cur.val) + " "
                cur = cur.next
            out += "\n"
        return out
'''

if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    param_2 = obj.get(12)
    print("gotten: ", param_2)

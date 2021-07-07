# HashMap class that handles the get, put, remove functions in 0(1) time


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 100151
        self.keys = [None] * self.capacity
        self.vals = [None] * self.capacity
        print(len(self.vals))

    # hash function designed to hold generate hash indices for strings and integers
    # will include one for handling float numbers next time
    def Hash(self, key):
        if type(key) == int:
            return key % self.capacity
        if type(key) == str:
            Hash = 0
            for i in key:
                Hash = (Hash + ord(i) * 256) % self.capacity
            return Hash
        else:
            return

    # if the index previously generated is already occupied, generate another hash index
    def rehash(self, oldhash):
        return (oldhash + 1) % self.capacity

    # to be implemented
    # if the hashmap is full, double the size then rehash every key
    def rehash(self):
        pass

    # put the key, value into hashmap if absent, otherwise change the value
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = self.Hash(key)
        if self.keys[idx] is None:
            self.keys[idx] = key
            self.vals[idx] = value
        elif self.keys[idx] == key:
            self.vals[idx] = value
        else:
            print("before rehashing: ", idx)
            last = idx
            idx = self.rehash(idx)
            print("after rehashing: ", idx)
            while self.keys[idx] != key and not self.keys[idx] and idx != last:
                idx = self.rehash(idx)
            if self.keys[idx] == key:
                self.vals[idx] = value
            elif self.keys[idx] is None:
                self.keys[idx] = key
                self.vals[idx] = value
            else:
                print("it's now full. rehash everything!!")

    # returns a string representation of the hashmap
    def __str__(self):
        for i, j in zip(self.keys, self.vals):
            if i is not None: print("val:", str(i) + "    key: ", j)

    # if the value is in the hashmap, return it
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = self.Hash(key)
        if self.keys[idx] == key:
            return self.vals[idx]
        else:
            last = idx
            idx = self.rehash(idx)
            while self.keys[idx] != key and idx != last:
                if self.keys[idx] is None: return -1
                idx = self.rehash(idx)
            if self.keys[idx] == key:
                return self.vals[idx]
            else:
                return -1

    # remove and return the value of the provided key if it is in the hashmap
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = self.Hash(key)
        if self.keys[idx] == key:
            self.keys[idx] = self.vals[idx] = None
        else:
            last = idx
            idx = self.rehash(idx)
            while self.keys[idx] != key and idx != last:
                if self.keys[idx] is None: return
                idx = self.rehash(idx)
            if self.keys[idx] == key:
                self.keys[idx] = self.vals[idx] = None
            else:
                return

# main method for unit testing
def main():
        obj = MyHashMap()
        print(obj.Hash(8))
        obj.put(1, 1)
        obj.put(2, 2)
        obj.put(3, 3)
        obj.put(3, 5)
        obj.__str__()


if __name__ == '__main__':
    main()

'''
Attempt


'''


class SegmentTree:
    def __init__(self, size):
        self.tree = [0 for _ in range(2*size+1)]

    def construct_tree(self, arr, idx, left, right):
        if left == right:
            self.tree[idx] = None

    def query_tree(self, idx):
        pass

    def update_tree(self, idx, val):
        root = self.tree

        def recurse_down(idx, target):
            if idx == target:
                self.tree[idx] = val
                return
            if idx:
                pass

        recurse_down(0, len(self.tree)//2 + idx)
        pass


if __name__ == 'main':
    seg = SegmentTree(10)
    arr = [1,2,3,4,5]
    seg.construct_tree(arr)

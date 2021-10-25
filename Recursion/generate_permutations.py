def generate__permutations(arr):
    res = []

    def permutate(start, part=[]):
        if start + 1 == len(arr):
            res.append(list(arr))
            return
        for i in range(start, len(arr)):
            arr[i], arr[start] = arr[start], arr[i]
            permutate(start+1)
            arr[i], arr[start] = arr[start], arr[i]

    def permutate_2(arr, part=[]):
        if len(arr) == 0:
            res.append(list(part))
            return
        for i in range(len(arr)):
            permutate_2(arr[:i]+arr[i+1:], part + [arr[i]])
    permutate_2(arr)
    return res


arr = [2, 3]
res = generate__permutations(arr)
print(res)

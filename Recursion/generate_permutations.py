def generate__permutations(arr):
    res = []
    def permutate(start, part=[]):
        if start + 1 ==len(arr):
            res.append(list(arr))
            return
        for i in range(start,len(arr)):
            arr[i], arr[start] = arr[start], arr[i]
            permutate(start+1)
            arr[i], arr[start] = arr[start], arr[i]
    def permutate_2(start, part=[]):
        if len(part)==len(arr):
            res.append(part)
            return
        for i in range(start, len(arr)):
            part.append(arr[start])
            permutate_2(start+1, list(part))
            part.pop()

    permutate(0)
    return res

arr = [2,3,5,7]
res = generate__permutations(arr)
print(res)
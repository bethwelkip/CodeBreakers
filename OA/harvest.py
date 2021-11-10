'''
[1, 5, 1, 3, 7.-3], L = 6, K = 2




'''


def max_profit(k, arr):
    if k == len(arr)//2:
        return sum(arr)

    start = 0
    n = len(arr)
    max_p = float('-inf')
    while start < len(arr)//2:
        curr = 0
        for i in range(k):
            j = (start + i) % n
            z = (j + n//2) % n
            curr += arr[j] + arr[z]
            print(start, j, z, n)
        max_p = max(curr, max_p)
        start += 1
    return max_p


def max_profit_efficient(k, arr):
    n = len(arr)

    prefill = [0 for _ in range(2*n+1)]
    for i in range(n+1):
        prefill[i] = arr[i]

        pass
    pass


arr = [1, 5, 1, 3, 7, -3]
arrb = [3, -5]
arrc = [-6, 3, 6, -3]
print(max_profit(1, arr))
print(max_profit(1, arrc))

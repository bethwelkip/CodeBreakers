'''
[1, 5, 1, 3, 7.-3], L = 6, K = 2




'''
import time

def max_profit(k, arr):
    if k == len(arr)//2:
        return sum(arr)
    z = 1
    start = 0
    n = len(arr)
    max_p = float('-inf')
    while start < len(arr)//2:
        curr = 0
        for i in range(k):
            # print(z)
            z += 1
            j = (start + i) % n
            z = (j + n//2) % n
            curr += arr[j] + arr[z]
        max_p = max(curr, max_p)
        start += 1
    return max_p


def max_profit_efficient(k, arr):
    n = len(arr)
    print('\n')
    total_sum = [0 for _ in range(2*n + 1)]
    for i in range(n):
        total_sum[i + 1] = total_sum[i] + arr[i]
    for i in range(n):
        total_sum[i + n + 1] = total_sum[i + n] + arr[i]

    i, j = 0, len(arr)//2
    max_profit = float('-inf')
    while i < (len(arr) // 2):
        curr_sum = (total_sum[i + k] - total_sum[i]) +(total_sum[i + j + k] - total_sum[i + j])
        max_profit = max(max_profit, curr_sum)
        i += 1

    return max_profit


arr = [1, 5, 1, 3, 7, -3]
arrb = [3, -5]
arrc = [-6, 3, 6, -3]
t1 =time.time()
for i in range(2000):
    max_profit(1, arr)
    t2= time.time()
    t3 = time.time()
    max_profit_efficient(1, arr)
    t4 = time.time()

    print((t2-t1)>(t4-t3))
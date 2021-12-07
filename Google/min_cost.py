'''
You are given a string consists of only 'a' and 'b'. Find the minimum cost to make the string contains only 'a'. You can do any number of the following operations:

Remove a character from the two ends of the string. Cost 1.
Remove a character from anywhere (not from the two ends). Cost 2.
Case 1:
Given 'abba'. Expect 3.

Case 2:
Given 'aaabbaaa'. Expect 4.

'''

def recursive_min_cost(s):
    idxs = [i for i, ch in enumerate(s) if ch == 'b']

    def recurse(cost, n, s):
        if n == 0 or len(s) == 0:
            return cost
        if s[0] == 'b':
            cost = recurse(cost+1, n-1, s[1:])

        elif s[-1] == 'b':
            cost = recurse(cost+1, n-1, s[:-1])
        else:
            idx = s.index('b')
            cost = min(
                recurse(cost+2, n-1, s[:idx]+s[idx+1:]), recurse(cost+1, n, s[1:]))
        return cost
    return recurse(0, len(idxs), s)
def count_b(s):
    pass

def dp_min_cost(s):
    costs = [float('inf') for _ in range(len(s))]*len(s)
    b_counts = count_b(s)

    for i,ch in enumerate(s):
        if ch == 'a':
            costs[i][i] = 0
        else:
            costs[i][i] = 1
    for i in range(len(s)):
        for j in range(len(s)-i):
            k = i+j
            costs[i][k] = b_counts[(i, j)]*2
            if k - 1 > 0:
                costs[i][k] = min(costs[i][k], costs[i][k-1]+1)
            if k + 1 < len(s):
                costs[i][k] = min(costs[i][k], costs[i+1][k]+1)
    return costs[0][-1]





    pass
print(recursive_min_cost('aaabbbbbaaaaaaaaaaaaaaaaabbbbbaaa'))

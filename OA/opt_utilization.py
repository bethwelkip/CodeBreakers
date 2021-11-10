'''
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. 
Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. 
Return a list of ids of selected elements. If no pair is possible, return an empty list.

Example 1:

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

Output: [[3, 1]]

Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]



'''

# bruteforce solution


def optimal_sum(a: list(), b: list, target: int):
    a.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[1])
    opt = []
    curr_min = 0
    min_x, min_y = None, None
    for x, y in a:
        for j, k in b:
            curr = k+y
            if curr == target:
                opt += [[x, j]]
            elif curr < target and curr > curr_min:
                curr_min = curr
                min_x, min_y = x, j

    if len(opt) == 0 and x is not None:
        return [[min_x, min_y]]
    else:
        return opt


arr_a = [[[1, 2], [2, 4], [3, 6]], [[1, 2]], 7]
arr_b = [[[1, 3], [2, 5], [3, 7], [4, 10]],
         [[1, 2], [2, 3], [3, 4], [4, 5]], 10]
arr_c = [[[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]], 20]
arr_d = [[[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]], 20]
arr = [arr_a, arr_b, arr_c, arr_d]

for a, b, target in arr:
    print(optimal_sum(a, b, target))

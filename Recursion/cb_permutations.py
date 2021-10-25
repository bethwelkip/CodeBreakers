"""
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

[123, 213, 132, 321, 231, 312]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

n! = 6
"""


def permutate(arr):
    res = []

    def swap(idx):
        if idx == len(arr):
            res.append(list(arr))
            return
        for i in range(idx, len(arr)):
            arr[i], arr[idx] = arr[idx], arr[i]
            swap(idx+1)
            arr[i], arr[idx] = arr[idx], arr[i]
    swap(0)
    return res


res = permutate([1, 2, 3])

print(res)

result = []


def permutation(nums):
    path = []
    if not nums:
        return result.append(path)

    backtrack(nums, [])
    return result


def backtrack(nums, path):
    if not nums:
        result.append(path)
    for i in range(len(nums)):
        print(len(nums))
        backtrack(nums[:i] + nums[i+1:], path + [nums[i]])


print(permutation([1, 1, 3]))

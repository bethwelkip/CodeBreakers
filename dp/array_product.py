'''
Given an array A[] of positive integers, return an array of integers whose k'th element is equal to the product of every integer in A[] except for the k'th element in A[].

Example #1:
Input: [1, 1, 2, 5]
Output: [10, 10, 5, 2]
'''


class Solution:
    def productExceptCurrentElement(self, arr):
        '''
        :type arr: list of int
        :rtype: list of int
        '''
        res = [1]*len(arr)
        last_idx = len(arr)-1

        pref = [1]*len(arr)
        pref[0] = arr[0]

        suf = [1]*len(arr)
        suf[-1] = arr[-1]

        for i in range(1, len(arr)):
            pref[i] = pref[i-1]*arr[i]

        for i in range(len(arr)-2, -1, -1):
            suf[i] = suf[i+1]*arr[i]

        for i in range(len(arr)):
            if i != 0:
                res[i] *= pref[i-1]
            if i != last_idx:
                res[i] *= suf[i+1]

        return res


arr = [1, 2, 3]
sol = Solution()
res = sol.productExceptCurrentElement(arr)
print(res)

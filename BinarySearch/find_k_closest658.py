class Solution:
    def findClosestElements(self, arr: list, k: int, x: int) -> list:

        # 1. do binary search to find where the element would appear
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right-left)//2
            if arr[mid] >= x:
                right = mid
            else:
                left = mid + 1
        ctr = left  # this is right most position of the value x

        left -= 1
        for _ in range(k):
            if left == -1:
                ctr += 1
            elif ctr == len(arr):
                left -= 1
            else:
                if abs(x-arr[left]) <= abs(arr[ctr]-x):
                    left -= 1
                else:
                    ctr += 1
        return arr[left+1:ctr]
    '''
    [0,0,1,2,3,3,4,7,7,8]
3
5
    
    '''

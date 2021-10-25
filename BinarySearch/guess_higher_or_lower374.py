class Solution:
    def guess(self, int) -> int:
        pass

    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right-left)//2

            if self.guess(mid) <= 0:
                right = mid
            else:
                left = mid + 1
        return left

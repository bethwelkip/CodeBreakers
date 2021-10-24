class Solution:
    def shipWithinDays(self, weights: list, days: int) -> int:
        def canShip(capacity: int) -> bool:
            d = 1
            weigh = 0
            for w in weights:
                weigh += w
                if weigh > capacity:
                    weigh = w
                    d += 1
                    if d > days:
                        return False
            return True

        left, right = max(weights), sum(weights)

        while left < right:
            mid = left + (right-left)//2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        return left

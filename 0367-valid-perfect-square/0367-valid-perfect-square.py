class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = low + (high-low)//2
            sq = mid*mid
            if sq == num:
                return True
            elif sq > num:
                high = mid - 1
            else:
                low = mid + 1
        return False        
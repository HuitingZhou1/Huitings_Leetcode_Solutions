class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = (low+high)//2
            if mid*mid == x or (mid*mid < x and (mid+1) * (mid+1) > x):
                return mid
            elif mid*mid < x:
                low = mid + 1
            else:
                high = mid - 1
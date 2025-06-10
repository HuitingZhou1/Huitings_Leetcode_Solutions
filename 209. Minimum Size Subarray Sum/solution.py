class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, sum, minl = 0,0,float('inf')

        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minl = min(minl, r-left+1)
                sum -= nums[left]
                left += 1
        
        return 0 if minl == float(inf) else minl
                

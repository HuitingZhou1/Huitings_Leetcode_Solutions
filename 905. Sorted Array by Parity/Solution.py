class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        output = [0] * len(nums)
        k = 0
        while (k < len(nums)):
            if nums[k] %2 == 0:
                output[left] = nums[k]
                left +=1
            else:
                output[right] = nums[k]
                right -=1
            k+=1
        return output
        
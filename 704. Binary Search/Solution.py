class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums)-1;
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid +1
            elif nums[mid] > target:
                high = mid -1
            if nums[mid] == target:
                return mid
        return -1
        
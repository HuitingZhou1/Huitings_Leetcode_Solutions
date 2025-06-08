class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_h = nums[:k]
        heapq.heapify(min_h)

        for num in nums[k:]:
            heapq.heappushpop(min_h, num)

        return min_h[0]
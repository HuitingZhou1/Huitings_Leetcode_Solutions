class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size()-1;
        while(left<=right) {
            int mid = (left+right)/2;
            if(nums[mid] == target) return mid;
            if(nums[left] <= nums[mid]) {
                if(nums[left] <= target && target < nums[mid]){
                    right =  mid-1;
                    continue;
                } else {
                    left = mid+1;
                    continue;
                }
            } else {
                if (nums[mid] <= target && target <= nums[right]) {
                    left = mid+1;
                    continue;
                } else {
                    right = mid -1;
                    continue;
                }
            }
        }

        return -1;
    }
};
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        if(target < nums[0]) return 0;
        if(target > nums.back()) return nums.size();
        while(left <= right) {
            int mid = (left + right)/2;
            if(nums[mid]==target) return mid;
            else if (nums[mid] < target) {
                if (mid+1 < nums.size()  && nums[mid+1] > target) {
                    return mid+1;
                }
                left = mid+1;
            }
            else if (nums[mid] > target) {
                if (mid-1 >0 && nums[mid-1] < target) {
                    return mid;
                }
                right = mid-1;
            }
        }
        return -1;
    }
};
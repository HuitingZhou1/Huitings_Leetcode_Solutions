class Solution {
public:
    int partition(vector<int>& nums, int left, int right) {
    int pivotIndex = left + rand() % (right - left + 1);  
    int pivotValue = nums[pivotIndex];
    swap(nums[pivotIndex], nums[right]);  

    int storeIndex = left;
    for (int i = left; i < right; i++) {
        if (nums[i] < pivotValue) {  
            swap(nums[i], nums[storeIndex]);
            storeIndex++;
        }
    }
    swap(nums[storeIndex], nums[right]); 
    return storeIndex; 
    }
int quickSelect(vector<int>& nums, int left, int right, int k_smallest) {
    if (left == right) return nums[left]; 

    int pivotIndex = partition(nums, left, right);

    if (pivotIndex == k_smallest) {
        return nums[pivotIndex]; 
    } else if (pivotIndex < k_smallest) {
        return quickSelect(nums, pivotIndex + 1, right, k_smallest);
    } else {
        return quickSelect(nums, left, pivotIndex - 1, k_smallest);
    }
}
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        int target = n-k;
        return quickSelect(nums, 0, n-1, target);
    }
        
};

#Runtime: 2195ms Beats:5.00%
#Memory: 59.14MB Beats:91.74%
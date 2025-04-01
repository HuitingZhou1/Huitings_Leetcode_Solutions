class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>,greater<int>> min_heap;
        for(auto num : nums) {
            min_heap.push(num);
            if(min_heap.size()>k) {
                min_heap.pop();
            }
        }
        return min_heap.top();
    }
};

#Runtime: 37ms Beats:38.69%
#Memory: 61.50MB Beats:43.27%
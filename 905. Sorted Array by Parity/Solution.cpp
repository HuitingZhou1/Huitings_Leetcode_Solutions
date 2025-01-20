class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int> v;
        for(int num:nums) {
            if(num%2==0) v.push_back(num);
        }
        for(int num:nums) {
            if(num%2!=0) v.push_back(num);
        }
        return v;
    }
};
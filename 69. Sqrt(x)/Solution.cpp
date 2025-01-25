class Solution {
public:
    int mySqrt(int x) {
        int right = x; 
        int left = 0;
        int result = 0;
        while(left <= right) {
            int mid = left + (right - left) / 2;
            long long square = (long long)mid * mid;
            if(square == x) {
                return mid;
            }
            if(square < x) {
                result = mid;
                left = mid+1;
            }
            if(square > x) right = mid -1;
        }
        return result;
    }
};
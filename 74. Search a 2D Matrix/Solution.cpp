class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int num_rows = matrix.size(),
        num_cols = matrix[0].size(),
        row = 0,
        col = num_cols - 1;

        while(row< num_rows && col > -1 ) {
            int cur = matrix[row][col];
            if(cur == target) {
                return true;
            }
            if(cur > target) col--;
            else row++;
        }
        return false;
    }
};
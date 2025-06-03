class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow, hrow = 0, len(matrix) - 1
        while lrow <= hrow:
            mrow = (lrow + hrow) // 2
            if matrix[mrow][0] > target:
                hrow = mrow - 1
            elif matrix[mrow][-1] < target:
                lrow = mrow + 1
            else:
                lcol, hcol = 0, len(matrix[0]) - 1
                while lcol <= hcol:
                    mcol = (lcol + hcol) // 2
                    if matrix[mrow][mcol] == target:
                        return True
                    elif matrix[mrow][mcol] > target:
                        hcol = mcol - 1
                    else:
                        lcol = mcol + 1
                return False
        return  False
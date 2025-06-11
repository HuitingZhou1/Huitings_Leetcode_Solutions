from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            res += matrix[top][left:right+1]
            top += 1

            res += [matrix[i][right] for i in range(top, bottom+1)]
            right -= 1

            if top <= bottom:
                res += [matrix[bottom][i] for i in range(right, left-1, -1)]
                bottom -= 1

            if left <= right:
                res += [matrix[i][left] for i in range(bottom, top-1, -1)]
                left += 1

        return res

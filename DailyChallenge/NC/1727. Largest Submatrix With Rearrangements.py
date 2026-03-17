from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Build heights
        heights = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[i][j] = heights[i-1][j] + 1 if i > 0 else 1
        
        max_area = 0
        
        # Step 2 & 3: Sort each row and compute max area
        for i in range(m):
            row = sorted(heights[i], reverse=True)
            for j in range(n):
                max_area = max(max_area, row[j] * (j + 1))
        
        return max_area

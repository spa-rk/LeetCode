class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        row, col = 0, 0 
        dir_x, dir_y =  0, 1 
        n, m = len(matrix), len(matrix[0])
        for _ in range(n*m): 
            result.append(matrix[row][col]) 
            matrix[row][col] = 0
            if not 0 <= row + dir_x < n or not 0 <= col + dir_y < m or matrix[row+dir_x][col+dir_y] == 0:
                dir_x, dir_y = dir_y, -dir_x 
            row, col = row + dir_x, col + dir_y
        return result
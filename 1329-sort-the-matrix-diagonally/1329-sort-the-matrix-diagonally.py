class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])        
        
        def sort_diagnoal(r, c):
            locations = []
            vals = []
            
            while r < R and c < C:
                locations.append([r, c])
                vals.append(mat[r][c])
                r += 1
                c += 1
            
            vals.sort()
            
            for loc, val in zip(locations, vals):
                mat[loc[0]][loc[1]] = val
                
        for col in range(C):
            sort_diagnoal(0, col)        
        
        for row in range(1, R):
            sort_diagnoal(row, 0)
        
        return mat
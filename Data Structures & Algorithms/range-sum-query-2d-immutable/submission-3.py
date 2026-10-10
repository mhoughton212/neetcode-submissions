class NumMatrix:

    def __init__(self, grid: List[List[int]]):
        N = len(grid)
        M = len(grid[0])
        self.prefix_grid = [[0] * M for i in range(N)] 
        for i in range(N):
            for j in range(M):
                self.prefix_grid[i][j] = (
                (self.prefix_grid[i][j - 1] if j else 0) + 
                (self.prefix_grid[i - 1][j] if i else 0) -
                (self.prefix_grid[i - 1][j - 1] if i and j else 0) +
                grid[i][j])
            
            
        print(self.prefix_grid)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix_grid[row2][col2] - 
                (self.prefix_grid[row2][col1 - 1] if col1 else 0) -
                (self.prefix_grid[row1 - 1][col2] if row1 else 0) +
                (self.prefix_grid[row1 - 1][col1 - 1] if row1 and col1 else 0))

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
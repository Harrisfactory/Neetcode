class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        Islands = []

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                curIsland = self.dfs(row, col, grid)
                if curIsland > 0:
                    Islands.append(curIsland)
        
        return max(Islands, default=0)

    def dfs(self, row, col, grid):
        #setup bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == 0:
            return 0
        
        #sink current island piece
        grid[row][col] = 0

        islandAreaCount = 1

        #traverse adj pieces to count/sink them
        islandAreaCount+=self.dfs(row - 1, col, grid)
        islandAreaCount+=self.dfs(row + 1, col, grid)
        islandAreaCount+=self.dfs(row, col - 1, grid)
        islandAreaCount+=self.dfs(row, col + 1, grid)

        return islandAreaCount

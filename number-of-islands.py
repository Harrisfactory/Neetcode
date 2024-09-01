class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        islandCounter = 0

        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                #detect island
                if grid[row][col] == "1":
                    #process island
                    self.dfs(row, col, grid, visited)
                    islandCounter+=1
        
        return islandCounter
    
    def dfs(self, row, col, grid, visited):
        #set bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == "0" or (row, col) in visited:
            return
        
        #destroy island piece
        grid[row][col] = "0"
        visited.add((row, col))

        #search for adjacent island pieces
        self.dfs(row - 1, col, grid, visited)
        self.dfs(row + 1, col, grid, visited)
        self.dfs(row, col - 1, grid, visited)
        self.dfs(row, col + 1, grid, visited)

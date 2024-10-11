class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        #setting up a visited tracker so we dont double dip
        visited = set()

        perimCount = 0
        
        #first we are going to create a cycle for our matrix
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimCount += self.dfs(grid, i, j, visited)
        return perimCount
    
    def dfs(self, grid, row, col, visited):
        #check bounds before compute
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or (row,col) in visited or grid[row][col] == 0:
            return 0
        
        #add to visited
        visited.add((row,col))

        curCount = 0

        #check perim
        if row - 1 < 0 or grid[row - 1][col] ==  0:
            curCount+=1
        if row + 1 > len(grid) - 1 or grid[row + 1][col] ==  0:
            curCount+=1
        if col - 1 < 0 or grid[row][col - 1] ==  0:
            curCount+=1
        if col + 1 > len(grid[row]) - 1 or  grid[row][col + 1] ==  0:
            curCount+=1

        #dfs
        curCount+=self.dfs(grid, row + 1, col, visited)
        curCount+=self.dfs(grid, row - 1, col, visited)
        curCount+=self.dfs(grid, row, col + 1, visited)
        curCount+=self.dfs(grid, row, col - 1, visited)
        
        return curCount

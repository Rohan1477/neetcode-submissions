class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        count = 0
        
        def dfs(r,c):
            if (r >= ROWS or c >= COLUMNS or r < 0 or c <0 or grid[r][c] == "0" or r < 0 or c < 0):
                return

            grid[r][c] = "0"

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    count +=1


        return count


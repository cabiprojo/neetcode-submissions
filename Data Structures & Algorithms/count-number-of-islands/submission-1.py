class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        total = 0

        def dfs(r, c):

            grid[r][c] = "0"
            
            # look at all adjacent spots within bounds
            if r < rows - 1 and grid[r+1][c] == "1": dfs(r + 1, c)
            if r > 0 and grid[r-1][c] == "1": dfs(r - 1, c)
            if c < cols - 1 and grid[r][c+1] == "1": dfs(r, c + 1)
            if c > 0 and grid[r][c-1] == "1": dfs(r, c - 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    total += 1

        return total

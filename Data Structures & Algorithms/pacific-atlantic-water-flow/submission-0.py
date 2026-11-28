class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacificVisit = set()
        atlanticVisit = set()

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        # top and bottom edges
        for r in range(rows):
            dfs(r, 0, pacificVisit, heights[r][0])
            dfs(r, cols - 1, atlanticVisit, heights[r][cols - 1])

        # left and right edges
        for c in range(cols):
            dfs(0, c, pacificVisit, heights[0][c])
            dfs(rows - 1, c, atlanticVisit, heights[rows - 1][c])

        # iterate through each cell and call helper function
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacificVisit and (r, c) in atlanticVisit:
                    res.append([r, c])

        return res

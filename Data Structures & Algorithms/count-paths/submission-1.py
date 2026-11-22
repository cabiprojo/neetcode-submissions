class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
  
        dp = [[1] * n for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m-1][n-1]

       
        ''' top-down
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1

        def dfs(r, c):
            # out of bounds
            if r >= m or c >= n:
                return 0

            # already calculated
            if dp[r][c] != 0:
                return dp[r][c]
            
            dp[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return dp[r][c]

        return dfs(0, 0)
        '''

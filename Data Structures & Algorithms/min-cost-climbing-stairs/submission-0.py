class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]

        for i in range(1, len(cost)):
            dp[i] = min(cost[i] + dp[i-2], cost[i] + dp[i-1])

        return min(dp[-1], dp[-2])
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        # run including first house, not last
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(1, len(nums)-1):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        
        amt1 = dp[-2]
        
        # run including last house, not first
        dp = [0] * len(nums)
        dp[1] = nums[1]
        dp[2] = nums[2]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])

        amt2 = dp[-1]

        return max(amt1, amt2)

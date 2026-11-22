class Solution:
    def numDecodings(self, s: str) -> int:
        # base case of how many decodings for empty string (1)
        dp = { len(s) : 1 }

        def dfs(i):
            if i in dp:
                return dp[i] # return cached number of decodings starting at index i
            if s[i] == "0":
                return 0 # standalone 0 cannot be decoded

            res = dfs(i + 1) # decode current digit individually
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2) # decode current and next digits together

            dp[i] = res # cache total number of decodings starting at index i
            return res

        return dfs(0) # return total number of decodings for entire string
        
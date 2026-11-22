class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [None] * (len(s)+1)
        dp[-1] = True

        def dfs(i):
            if dp[i] is not None:
                return dp[i]

            # check if a word aligns at s[i]
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if dfs(i + len(word)):
                        dp[i] = True
                        return True
                
            dp[i] = False
            return False

        return dfs(0)

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, i):
            if sum(path) == target: 
                res.append(path.copy())
                return

            if sum(path) > target or i >= len(nums):
                return

            path.append(nums[i])
            backtrack(path, i)
            path.pop()
            backtrack(path, i + 1)
            
        backtrack([], 0)
        return res
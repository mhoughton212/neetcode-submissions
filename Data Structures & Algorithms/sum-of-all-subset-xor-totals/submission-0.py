class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def dfs(i, xor):
            if i >= len(nums):
                res.append(xor)
                return
            
            xor ^= nums[i]
            dfs(i + 1, xor)

            xor ^= nums[i]
            dfs(i + 1, xor)
            

        dfs(0, 0)
        return sum(res)
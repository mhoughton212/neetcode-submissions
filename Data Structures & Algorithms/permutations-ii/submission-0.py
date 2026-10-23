class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        used = [False] * len(nums)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                #[1,1]
                perm.append(nums[i])
                used[i] = True
                dfs()
                perm.pop()
                used[i] = False

        nums.sort()
        dfs()
        return res
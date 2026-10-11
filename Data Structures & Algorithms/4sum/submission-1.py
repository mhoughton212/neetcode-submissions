class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                l = j + 1
                r = n - 1
                #[-1,-1,-1,1,1,1]
                while l < r:
                    curr = nums[i] + nums[j] + nums[l] + nums[r]
                    if curr == target:
                        res.add(tuple(sorted([nums[i], nums[j], nums[l], nums[r]])))
                        l += 1
                        r -= 1
                    elif curr < target:
                        l += 1
                    else:
                        r -= 1
        
        return list(res)

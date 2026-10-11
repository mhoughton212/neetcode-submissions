class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if not curr:
                    res.add((nums[i], nums[l], nums[r]))
                    r -= 1
                elif curr > 0:
                    r -= 1
                else:
                    l += 1

        return [list(i) for i in res]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0
        curr_streak = 0
        for num in nums:
            curr_streak = 0
            if num - 1 not in nums_set:
                while num in nums_set:
                    curr_streak += 1
                    num += 1
                res = max(res, curr_streak)
        return res
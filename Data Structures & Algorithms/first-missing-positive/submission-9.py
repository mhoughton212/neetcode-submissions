class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(len(nums)):
            if i + 1 not in nums_set:
                return i + 1

        return len(nums) + 1

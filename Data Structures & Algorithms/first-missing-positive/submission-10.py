class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = (len(nums) + 1)

        for i in range(len(nums)):
            val = abs(nums[i])
            if abs(val) < len(nums) + 1:
                nums[val - 1] = -abs(nums[val - 1])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1

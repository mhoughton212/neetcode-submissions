class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            val = abs(nums[i])
            if val > 0 and val <= len(nums):
                idx = val - 1
                if nums[idx] == 0:
                    nums[idx] = -len(nums) - 1
                elif nums[idx] > 0:
                    nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        
        return len(nums) + 1

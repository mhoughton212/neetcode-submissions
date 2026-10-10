class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        ans = []
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in num_to_index:
                return [num_to_index[compliment], i]
            num_to_index[num] = i
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(nums):
            if len(nums) <= 1:
                return nums
            pivot = int(random.random() * len(nums))
            left = []
            right = []
            middle = []
            for i in nums:
                if i < nums[pivot]:
                    left.append(i)
                elif i > nums[pivot]:
                    right.append(i)
                else:
                    middle.append(i)
            return quickSort(left) + middle + quickSort(right)

        return quickSort(nums)
        
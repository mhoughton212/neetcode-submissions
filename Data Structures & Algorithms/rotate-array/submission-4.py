class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0] * len(nums)
        for i in range(len(nums)):
            new_i = (i + k) % len(nums)
            temp[new_i] = nums[i]

        nums[:] = temp
        return
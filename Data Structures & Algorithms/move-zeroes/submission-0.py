class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        [1,2,0,0,0,0]
        [0,0,1,2,5,0]
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
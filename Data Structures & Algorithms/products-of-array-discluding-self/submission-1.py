class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            #[1,2,4,6]
            #[1,1,12,8]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res 
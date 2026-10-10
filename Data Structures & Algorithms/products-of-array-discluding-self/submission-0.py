class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = prefix.copy()
        #[1, 2, 4, 6]
        #[1, 1, 2, 8, 48]
        #[48, 48, 24, 6, 1]
        for i in range(len(nums) - 1):
            prefix[i + 1] = prefix[i] * nums[i]
        
        for i in range(len(nums), 1, -1):
            suffix[i - 1] = suffix[i] * nums[i - 1]
        
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i + 1])
        return res

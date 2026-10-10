class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
[1,1,2,2,4]
[1,2,2,2,4]
[1,2,4,2,4]
        '''
        n = len(nums)
        if n < 2:
            return n
        l = 1
        for r in range(1, n):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l


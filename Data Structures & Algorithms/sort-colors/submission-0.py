class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in nums:
            count[i] += 1
        
        curr = 0
        for i in range(3):
            while count[i]:
                nums[curr] = i
                count[i] -= 1
                curr += 1
        
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        #[3,4,1,4] val = 1
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
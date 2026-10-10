class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for i in range(len(nums)):
            if nums[i] != val:
                temp.append(nums[i])
        nums[:] = temp
        return len(nums)
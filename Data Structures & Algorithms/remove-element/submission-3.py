class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        while j >= 0 and nums[j] == val:
            j -= 1

        for i in range(len(nums)):
            if i >= j:
                break
            if nums[i] == val:
                #swap
                nums[i] ^= nums[j]
                nums[j] ^= nums[i]
                nums[i] ^= nums[j]
                j -= 1
                while j >= 0 and nums[j] == val:
                    j -= 1
        i = 0
        while i < len(nums) and nums[i] != val:
            i += 1 
        return i
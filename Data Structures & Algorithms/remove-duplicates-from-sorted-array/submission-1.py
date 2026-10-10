class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = len(set(nums))
        nums[:res] = sorted(list(set(nums)))
        return res
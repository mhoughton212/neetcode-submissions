class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
            elif num >= 0 and num > res:
                return res

        return res
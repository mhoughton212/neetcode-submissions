class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        some_guy = 0
        for num in nums:
            if num == ans:
                some_guy += 1
            else:
                some_guy -= 1
            if some_guy < 0:
                ans = num
                some_guy = 1
        return ans
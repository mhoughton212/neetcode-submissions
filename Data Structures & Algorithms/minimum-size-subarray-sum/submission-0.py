class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        found = False
        curr = 0

        # [1000, 1]

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                found = True
                res = min(res, r - l + 1)

                curr -= nums[l]
                l += 1
                if l > r:
                    return 1

        return res if found else 0
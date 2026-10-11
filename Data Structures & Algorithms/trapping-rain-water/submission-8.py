class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l = height[l]
        max_r = height[r]
        res = 0

        while l < r:
            if max_l < max_r:
                l += 1
                res += max(0, max_l - height[l])
                max_l = max(max_l, height[l])
            else:
                r -= 1
                res += max(0, max_r - height[r])
                max_r = max(max_r, height[r])

        return res

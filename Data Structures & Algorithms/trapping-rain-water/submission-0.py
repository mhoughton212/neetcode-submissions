class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        res = 0
        
        curr = 0
        for i in range(1, len(height)):
            curr = max(height[i - 1], curr)
            prefix[i] = curr
        
        curr = 0
        for i in range(len(height) - 2, -1, -1):
            curr = max(height[i + 1], curr)
            suffix[i] = curr

        for i in range(len(height)):
            res += max(0, min(prefix[i], suffix[i]) - height[i])

        return res

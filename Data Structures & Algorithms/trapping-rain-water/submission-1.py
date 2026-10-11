class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        res = 0
        
        for i in range(1, len(height)):
            prefix[i] = max(height[i - 1], prefix[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(height[i + 1], suffix[i + 1])

        for i in range(len(height)):
            res += max(0, min(prefix[i], suffix[i]) - height[i])

        return res

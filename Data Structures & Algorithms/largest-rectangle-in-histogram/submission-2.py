class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][-1] > h:
                stack_i, stack_h = stack.pop()
                res = max(res, stack_h * (i - stack_i))
                start = stack_i
            stack.append((start, h))
        # print(stack)
        while stack:
            stack_i, stack_h = stack.pop()
            res = max(res, stack_h * (len(heights) - stack_i))
        return res


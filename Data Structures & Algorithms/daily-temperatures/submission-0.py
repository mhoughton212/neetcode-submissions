class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][-1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, temp))
        
        return res

        #[(1,38),(3,36)]
        #[1,0,1,2,1,0,0]
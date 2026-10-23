class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []
        
        def dfs(start):
            if start == len(s):
                res.append(partition.copy())
                return
            
            for i in range(start, len(s)):
                substr = s[start:i + 1]

                if substr != substr[::-1]:
                    continue
                
                partition.append(substr)
                dfs(i + 1)
                partition.pop()

        dfs(0)
        return res
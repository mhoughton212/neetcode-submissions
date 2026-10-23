class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        combo = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(combo))
                return
            
            for c in letters[int(digits[i]) - 2]:
                combo.append(c)
                dfs(i + 1)
                combo.pop()
        
        dfs(0)
        return res
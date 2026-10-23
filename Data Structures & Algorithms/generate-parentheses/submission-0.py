class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parenthesis = []

        def dfs(open_count, close_count):
            if close_count == n:
                res.append("".join(parenthesis))
                return
            
            if open_count < n:
                parenthesis.append("(")
                dfs(open_count + 1, close_count)
                parenthesis.pop()
            if close_count < open_count:
                parenthesis.append(")")
                dfs(open_count, close_count + 1)
                parenthesis.pop()
            
        dfs(0, 0)
        return res

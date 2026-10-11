class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for p in s:
            if p in p_map.keys():
                stack.append(p)
            else:
                if not stack or p != p_map[stack.pop()]:
                    return False 

        return not stack
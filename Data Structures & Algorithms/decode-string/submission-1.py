class Solution:
    def decodeString(self, s: str) -> str:
        curr = ""
        stack = []
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((num, curr))
                curr = ""
                num = 0
            elif c == "]":
                n, prev = stack.pop()
                curr = prev + curr * n
            else:
                curr += c

        return curr
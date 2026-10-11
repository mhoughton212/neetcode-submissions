class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []
        res = 0

        for t in tokens:
            if t in ops:
                second = stack.pop()
                first = stack.pop()
                if t == "+":
                    first += second
                elif t == "-":
                    first -= second
                elif t == "*":
                    first *= second
                else:
                    first = int(first / second)
                stack.append(first)
            else:
                stack.append(int(t))

        return stack[-1]
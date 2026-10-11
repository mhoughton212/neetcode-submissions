class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []
        res = 0

        for t in tokens:
            if t in ops:
                second = int(stack.pop())
                first = int(stack.pop())
                if t == "+":
                    first += second
                elif t == "-":
                    first -= second
                elif t == "*":
                    first *= second
                else:
                    first /= second
                stack.append(first)
            else:
                stack.append(t)

        return int(stack.pop())
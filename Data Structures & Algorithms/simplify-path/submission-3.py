class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for i in range(len(path)):
            if not path[i] or path[i] == ".":
                continue
            if path[i] == "..":
                if stack: stack.pop()
                continue
            stack.append(path[i])

        return "/" + "/".join(stack)
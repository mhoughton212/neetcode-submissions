class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def areValidPalindromes(partition):
            for s in partition:
                if s != s[::-1]:
                    return False
            return True

        res = []
        partition = []

        def dfs(i, curr):
            if i == len(s):
                if curr == curr[::-1]:
                    partition.append(curr)
                    res.append(list(partition))
                    partition.pop()
                return

            dfs(i + 1, curr + s[i])

            if curr == curr[::-1]:
                partition.append(curr)
                dfs(i + 1, s[i])
                partition.pop()

        dfs(1, s[0])
        return res
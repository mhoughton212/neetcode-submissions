class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        shortest = min(strs, key = len)
        for i in range(len(shortest)):
            c = shortest[i]
            for s in strs:
                if s[i] != c:
                    return ans
            ans += c
        return ans

        
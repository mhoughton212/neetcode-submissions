class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPali(l, r):
            return s[l:r+1] == s[l:r+1][::-1]
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return isPali(l + 1, r) or isPali(l, r - 1)
            l += 1
            r -= 1
        
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while not s[l].isalnum():
                l += 1
                if l == len(s):
                    return True
            while not s[r].isalnum():
                r -= 1
                if r == -1:
                    return True
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        while l <= r:
            m = (l + r) // 2
            candidate = m * m
            if candidate == x:
                return m
            elif candidate < x:
                l = m + 1
            else:
                r = m - 1

        return r
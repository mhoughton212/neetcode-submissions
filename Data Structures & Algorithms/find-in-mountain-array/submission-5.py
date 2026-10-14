from functools import cache

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 1, mountainArr.length() - 2

        @cache
        def get(i):
            return mountainArr.get(i)

        while l < r:
            m = (l + r) // 2
            lval, rval = get(m), get(m + 1)

            if lval < rval:
                l = m + 1
            else:
                r = m
            
        peak = l
        l, r = 0, peak

        while l <= r:
            m = (l + r) // 2
            val = get(m)

            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        l, r = peak + 1, mountainArr.length() - 1

        while l <= r:
            m = (l + r) // 2
            val = get(m)

            if val == target:
                return m
            elif val < target:
                r = m - 1
            else:
                l = m + 1

        return -1

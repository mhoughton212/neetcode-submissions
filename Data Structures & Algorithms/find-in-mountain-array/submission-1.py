class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 1, mountainArr.length() - 2

        while l <= r:
            m = (l + r) // 2
            lval, mval, rval = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)

            if lval < mval > rval:
                break
            elif lval < mval < rval:
                l = m + 1
            else:
                r = m - 1

            
        peak = m
        l, r = 0, peak

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        l, r = peak + 1, mountainArr.length() - 1

        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val == target:
                return m
            elif val < target:
                r = m - 1
            else:
                l = m + 1

        return -1

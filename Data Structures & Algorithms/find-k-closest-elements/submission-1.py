class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        target_idx = len(arr)

        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2

            if arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        
        target_idx = l

        lres = []
        rres = []
        l, r = target_idx - 1, target_idx
        while len(lres) + len(rres) < k:
            if l < 0:
                rres.append(arr[r])
                r += 1
            elif r > len(arr) - 1:
                lres.append(arr[l])
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                lres.append(arr[l])
                l -= 1
            else:
                rres.append(arr[r])
                r += 1

        return list(reversed(lres)) + rres
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #find index
        target_idx = len(arr)

        for i in range(len(arr)):
            if arr[i] >= x:
                target_idx = i
                break

        #expand outward until res has k elements
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

        #DONE!
        return list(reversed(lres)) + rres
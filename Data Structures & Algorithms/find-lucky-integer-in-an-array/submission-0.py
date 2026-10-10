class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)

        res = -1
        for key in counts:
            if key == counts[key]:
                res = max(res, key)
        
        return res
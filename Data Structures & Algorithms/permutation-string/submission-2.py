class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False

        counts1 = Counter(s1)
        counts2 = Counter(s2[:l1])
        # hi
        # hchungus
        for i in range(l1, l2):
            if counts1 == counts2:
                return True
            
            counts2[s2[i - l1]] -= 1
            counts2[s2[i]] += 1

        return counts1 == counts2
        
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for sc, tc in zip(s, t):
            if (sc in s_map and s_map[sc] != tc) or (tc in t_map and t_map[tc] != sc):
                return False
            s_map[sc] = tc
            t_map[tc] = sc
        return True
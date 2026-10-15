class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_counts, t_counts = defaultdict(int), Counter(t)
        have, need = 0, len(t_counts)
        res_idx, res_length = (0, 0), float('inf')
        l = 0

        for r in range(len(s)):
            rval = s[r]
            s_counts[rval] += 1
            if rval in t_counts and s_counts[rval] == t_counts[rval]:
                have += 1

            ""
            while have == need:
                if r - l + 1 < res_length:
                    res_length = r - l + 1
                    res_idx = (l, r)
                lval = s[l]
                s_counts[lval] -= 1
                if lval in t_counts and s_counts[lval] < t_counts[lval]:
                    have -= 1

                l += 1
        l, r = res_idx
        return s[l:r + 1] if res_length != float('inf') else ""

                    
            

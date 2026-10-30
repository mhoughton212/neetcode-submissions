class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = set(range(1, n + 1))
        trustees = defaultdict(int)

        for i in trust:
            trustor, trustee = i

            candidates.discard(trustor)
            trustees[trustee] += 1
        
        cand_list = list(candidates)
        return cand_list[0] if cand_list and trustees[cand_list[0]] == n - 1 else -1
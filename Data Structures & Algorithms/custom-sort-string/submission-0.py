class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = {}
        j = 0
        for i in order:
            rank[i] = j
            j += 1

        def get_rank(character):
            if character in rank:
                return rank[character]
            return 26
        
        return ''.join(sorted(s, key = get_rank))
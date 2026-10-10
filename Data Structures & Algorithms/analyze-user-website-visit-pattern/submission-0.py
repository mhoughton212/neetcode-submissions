class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        arr = list(zip(timestamp, username, website))
        arr.sort()

        user_visits = defaultdict(list)
        for t, u, w in arr:
            user_visits[u].append(w)

        counts = defaultdict(int)
        for user in user_visits:
            visits = user_visits[user]
            patterns = set()
            i = 0
            while i < len(visits) - 2:
                patterns.add((visits[i], visits[i + 1], visits[i + 2]))
                i += 1
            
            for pattern in patterns:
                counts[pattern] += 1

        return list(min(counts, key=lambda k: (-counts[k], k)))

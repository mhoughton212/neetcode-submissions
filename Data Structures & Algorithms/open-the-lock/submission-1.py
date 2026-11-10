class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
            
        visited = set()
        turns = 0
        q = deque(["0000"])
        
        while q:
            for _ in range(len(q)):
                combo = q.popleft()

                if combo == target:
                    return turns

                for i in range(4):
                    for sign in [-1, 1]:
                        digit = str((int(combo[i]) + sign) % 10)
                        turn = combo[:i] + digit + combo[i + 1:]
                        if turn not in visited and turn not in deadends:
                            q.append(turn)
                            visited.add(turn)

            turns += 1

        return -1
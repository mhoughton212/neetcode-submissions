class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        lightest = min(people)
        heaviest = max(people)
        counts = [0] * (heaviest - lightest + 1)

        for p in people:
            counts[p - lightest] += 1

        new_people = []
        for i in range(len(counts)):
            new_people.extend([i + lightest] * counts[i])

        res = 0
        l, r = 0, len(new_people) - 1
        while l <= r:
            if new_people[l] + new_people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1

            res += 1

        return res
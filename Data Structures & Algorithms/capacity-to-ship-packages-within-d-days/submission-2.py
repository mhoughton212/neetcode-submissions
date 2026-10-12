class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        while l <= r:
            m = (l + r) // 2
            days_so_far = 1
            weight = 0
            for i in range(len(weights)):
                if weight + weights[i] > m:
                    days_so_far += 1
                    weight = 0
                weight += weights[i]
            
            if days_so_far > days:
                l = m + 1
            else:
                r = m - 1
        
        return l
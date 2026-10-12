class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counts = defaultdict(list)

        for i in range(len(nums)):
            counts[nums[i]].append(i)
            
        for val, idxs in counts.items():
            if len(idxs) > 1:
                for i in range(1, len(idxs)):
                    if abs(idxs[i] - idxs[i - 1]) <= k:
                        return True
        
        return False
        #{1: [0,2,3], 0: [1]}
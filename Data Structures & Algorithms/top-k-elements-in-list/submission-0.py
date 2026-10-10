class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        heap = [(-freq, val) for val, freq in counts.items()]
        heapq.heapify(heap)
        ans = []
        for _ in range(k):
            freq, val = heapq.heappop(heap)
            ans.append(val)
        return ans

        # O(n) + O(n) + O(k * logd)
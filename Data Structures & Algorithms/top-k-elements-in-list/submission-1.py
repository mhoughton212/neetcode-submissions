class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for val, freq in counts.items():
            buckets[freq].append(val)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            res += buckets[i]
            if len(res) == k:
                return res
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        for val, freq in counts.items():
            if freq > len(nums) // 3:
                res.append(val)

        return res
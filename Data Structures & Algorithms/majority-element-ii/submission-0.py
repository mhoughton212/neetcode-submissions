class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        result = []

        threshold = len(nums) // 3
        for key, val in counts.items():
            if val > threshold:
                result.append(key)
        
        return result
        
        
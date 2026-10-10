class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        result = []

        for num in nums:
            count[num] += 1

            if len(count) < 3:
                continue
            
            new_count = defaultdict(int)
            for key in count:
                if count[key] > 1:
                    new_count[key] = count[key] - 1

            count = new_count

        
        for key in count:
            if nums.count(key) > len(nums) // 3:
                result.append(key)
            
        return result
        
        
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        res = []
        #{2:4, 5:3}
        #[]
        for num in nums:
            counts[num] += 1
            to_del = []
            if len(counts) > 2:
                for key in counts:
                    counts[key] -= 1
                    if counts[key] == 0:
                        to_del.append(key)
                for key in to_del:
                    del counts[key]

        for key in counts:    
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        return res 
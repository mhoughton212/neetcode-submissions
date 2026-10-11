class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        #[1,1,1,1,1], k = 3
        curr = 0
        #{0:1, }
        #2
        #1
        for i in range(len(nums)):
            curr += nums[i]
            res += prefix[curr - k]
            prefix[curr] += 1
        return res
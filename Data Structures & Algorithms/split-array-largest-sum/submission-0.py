class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def countSubarrays(m):
            subarrays = 1
            curr_sum = 0
            for num in nums:
                curr_sum += num

                if curr_sum > m:
                    subarrays += 1
                    curr_sum = num
            
            return subarrays
        
        l, r = max(nums), sum(nums)

        #l: everything before takes too many subarrays
        #r: everything after is fine but might be too greedy
        # [10,22] --> 16
        while l <= r:
            m = (l + r) // 2

            subarrays = countSubarrays(m)
            if subarrays > k:
                l = m + 1
            else:
                r = m - 1
        
        return r + 1
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        
        size = sum(nums) // k
        buckets = [0] * k

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if buckets[j] + nums[i] <= size:
                    buckets[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    buckets[j] -= nums[i]

                    if buckets[j] == 0:
                        return False
            return False

        return dfs(0)

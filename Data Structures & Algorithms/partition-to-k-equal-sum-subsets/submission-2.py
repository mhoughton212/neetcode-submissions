class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        
        size = sum(nums) // k
        buckets = [0] * k

        def dfs(i):
            if i == len(nums):
                return True

            seen = set()

            for j in range(k):
                if buckets[j] in seen:
                    continue
                if buckets[j] + nums[i] <= size:
                    seen.add(buckets[j])
                    buckets[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    buckets[j] -= nums[i]

            return False

        return dfs(0)

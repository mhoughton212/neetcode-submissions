class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sumSubArrays = defaultdict(int)
        sumSubArrays[0] = 1
        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]
            res += sumSubArrays[currSum - k]
            sumSubArrays[currSum] += 1


        return res
        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        #[1,0]
        #[2,1]
        for i in range(len(nums)):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()

            queue.append(i)
            if i - k >= queue[0]:
                queue.popleft()

            if i > k - 2:
                res.append(nums[queue[0]])

        
        return res
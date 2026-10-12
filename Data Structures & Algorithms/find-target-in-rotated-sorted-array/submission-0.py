class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l, r = 0, n - 1
        
        while l <= r:
            m = (l + r) // 2
            m_pivot = (m + pivot) % n

            if nums[m_pivot] == target:
                return m_pivot
            elif nums[m_pivot] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

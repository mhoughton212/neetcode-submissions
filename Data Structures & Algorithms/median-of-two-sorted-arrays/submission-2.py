class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)

        total_mid = (len1 + len2 + 1) // 2 #1

        l_bound = 0
        r_bound = len1

        while l_bound <= r_bound:
            m = (l_bound + r_bound) // 2 #0
            j = total_mid - m

            # 4 | 5 6
            # 0 | 1
            l1 = nums1[m - 1] if m - 1 >= 0 else float('-inf') #-inf
            r1 = nums1[m] if m < len1 else float('inf') #1
            l2 = nums2[j - 1] if j - 1 >= 0 else float('-inf') #-inf
            r2 = nums2[j] if j < len2 else float('inf') #4

            if l1 <= r2 and l2 <= r1:
                if (len1 + len2) % 2:
                    return float(max(l1, l2))
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2 
            elif l1 > r2:
                r_bound = m -1
            else:
                l_bound = m + 1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        replace = len(nums1) - 1
        ptr1 = len(nums1) - 1 - n
        ptr2 = len(nums2) - 1
        while ptr1 > -1 and ptr2 > -1:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[replace] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[replace] = nums2[ptr2]
                ptr2 -= 1
            replace -= 1
        
        while ptr2 > -1:
            nums1[replace] = nums2[ptr2]
            ptr2 -= 1
            replace -= 1
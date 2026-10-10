import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(some_nums):
            if not some_nums:
                return []

            pivot = random.choice(some_nums)
            smaller = []
            equal = []
            greater = []
            for num in some_nums:
                if num < pivot:
                    smaller.append(num)
                elif num == pivot:
                    equal.append(num)
                else:
                    greater.append(num)
            return quickSort(smaller) + equal + quickSort(greater)
        return quickSort(nums)

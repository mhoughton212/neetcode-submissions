class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestElements = [-1] * len(arr)
        greatestElement = -1

        # [-1, -1, -1, -1, -1, -1]
        for i in range(len(arr) - 2, -1, -1):
            greatestElement = max(greatestElement, arr[i + 1])
            greatestElements[i] = greatestElement
            

        return greatestElements
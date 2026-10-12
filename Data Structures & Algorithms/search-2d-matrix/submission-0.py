class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1

        while t <= b:
            row = (t + b) // 2
            small_val = matrix[row][0]
            big_val = matrix[row][-1]

            if target >= small_val and target <= big_val:
                l, r = 0, len(matrix[0]) - 1
                while l <= r:
                    col = (l + r) // 2
                    val = matrix[row][col]

                    if val == target:
                        return True
                    elif val < target:
                        l = col + 1
                    else:
                        r = col - 1
                
                return False

            elif small_val < target:
                t = row + 1

            else:
                b = row - 1

        return False

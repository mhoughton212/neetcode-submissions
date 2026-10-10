class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        # [[1], [1,1], [1,]]
        for i in range(1, numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(result[i - 1][j - 1] + result[i - 1][j])
            result.append(row)

        return result


        
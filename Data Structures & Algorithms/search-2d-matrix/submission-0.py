class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        index = 0
        for i in range(len(matrix)):
            lower = matrix[i][0]
            upper = matrix[i][-1]

            if target <= upper and target >= lower:
               index = i
               break

        else:
            return False

        row = matrix[index]

        start = 0
        end = len(row) - 1

        while start <= end:
            mid = (start+end)//2

            if row[mid] == target:
                return True

            elif row[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        return False
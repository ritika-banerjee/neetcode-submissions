class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        index = 0
        while start <= end:
            mid = (start+end) // 2
            lower = matrix[mid][0]
            upper = matrix[mid][-1]

            if target <= upper and target >= lower:
               index = mid
               break

            elif target > lower:
                start = mid + 1
                
            else:
                end = mid - 1

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
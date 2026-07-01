class Solution:
    def isValidSudoku(self, nums: List[List[str]]) -> bool:
        
        rows = len(nums[0])
        cols = len(nums[1])

        for row in range(rows):
            seen = set()
            for col in range(cols):
                if nums[row][col] == ".":
                    continue

                elif nums[row][col] in seen:
                    return False

                else:
                    seen.add(nums[row][col])

        for col in range(cols):
            seen = set()
            for row in range(rows): 
                if nums[row][col] == ".":
                    continue

                elif nums[row][col] in seen:
                    return False

                else:
                    seen.add(nums[row][col])
        

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()

                for r in range(3):
                    for c in range(3):
                        row = box_row + r
                        col = box_col + c

                        if nums[row][col] == ".":
                            continue

                        elif nums[row][col] in seen:
                            return False

                        else:
                            seen.add(nums[row][col])

        return True
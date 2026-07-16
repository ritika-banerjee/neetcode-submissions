class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1
        mid = (end+start)//2

        while start <= end:
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                end = mid - 1
                mid = (end+start)//2

            else:
                start = mid + 1
                mid = (end+start)//2

        return -1
            
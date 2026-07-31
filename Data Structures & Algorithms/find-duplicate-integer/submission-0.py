class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        freq = Counter(nums)

        for num, value in freq.items():
            if value > 1:
                return num

        return -1

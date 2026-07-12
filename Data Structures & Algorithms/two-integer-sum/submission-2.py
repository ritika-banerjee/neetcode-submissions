class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap ={}
        result = []

        for i in range(len(nums)):
            if target - nums[i] in hmap:
                result =[hmap[target- nums[i]], i]
                return result

            else:
                hmap[nums[i]] = i

        
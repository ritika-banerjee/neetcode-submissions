class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    triplet = [nums[i] , nums[j] , nums[k]]
                    j += 1
                    k -= 1
                    if triplet in result:
                        continue

                    result.append(triplet)

                elif total < 0:
                    j += 1

                else:
                    k -= 1

        return result
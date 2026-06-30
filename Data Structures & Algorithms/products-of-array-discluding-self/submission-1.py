class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)
        result = [1] * len(nums)

        left_prod[0] = 1
        right_prod[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            left_prod[i] = left_prod[i - 1] * nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            right_prod[i] = right_prod[i + 1] * nums[i+1]

        for i in range(len(nums)):
            result[i] = left_prod[i] * right_prod[i]

        print(left_prod)
        print(right_prod)
        print(result)

        return result

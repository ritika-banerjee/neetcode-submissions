# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = [0] * len(nums)

#         for num in nums:
#             counter[num] += 1

#         result = []

        
#         return result

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        return [key for key, frequency in sorted_counter[:k]]
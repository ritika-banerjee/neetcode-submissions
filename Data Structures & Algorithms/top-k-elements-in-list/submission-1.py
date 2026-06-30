from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in counter.items():
            bucket[freq].append(num)
        
        result = []

        for freq in range(len(bucket)-1, 0,-1):
            result.extend(bucket[freq])

            if len(result) >= k:
                return result[:k]

        
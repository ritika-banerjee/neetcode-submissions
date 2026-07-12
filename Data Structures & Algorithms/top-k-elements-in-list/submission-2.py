from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        result = []

        for key, value in counter.items():
            bucket[value].append(key)

        for i in range(len(bucket) - 1, 0, -1):
            result.extend(bucket[i])

            if len(result) >= k:
                return result[:k]
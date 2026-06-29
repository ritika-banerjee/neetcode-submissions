from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counter = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        results = [x for  x, _ in sorted_counter][:k]
        return results
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[] for _ in range(len(nums)+1)]
        frequencies = Counter(nums)
        result = []

        for num, freq in frequencies.items(): 
            bucket[freq].append(num)

        for i in range(len(bucket)-1, 0, -1):
            result.extend(bucket[i])

            if len(result) >= k:
                return result[:k]
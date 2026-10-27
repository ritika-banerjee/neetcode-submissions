class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        max_freq = max(counter.values())
        buckets = [[] for _ in range(max_freq+1)]

        for num, freq in counter.items():
            buckets[freq].append(num)

        result = []

        for i in range(len(buckets)-1, -1, -1):
            if len(result) >= k:
                break

            result.extend(buckets[i])

        return result


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = Counter(nums)
#         sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

#         return [key for key, frequency in sorted_counter[:k]]
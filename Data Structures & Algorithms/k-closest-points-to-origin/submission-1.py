class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for idx, point in enumerate(points):
            dist = point[0]**2 + point[1]**2
            heapq.heappush(heap, (-dist, idx))

            if len(heap) > k:
                heapq.heappop(heap)

        return [points[idx] for _, idx in heap]
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for idx, point in enumerate(points):
            dist = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            heapq.heappush(heap, (dist, idx))

        for i in range(k):
            idx = heapq.heappop(heap)[1]
            result.append(points[idx])
        
        print(result)
        return result
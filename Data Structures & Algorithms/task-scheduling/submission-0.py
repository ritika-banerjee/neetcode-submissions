class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)
        
        cooldown = deque()

        time = 0

        while heap or cooldown:

            if cooldown and cooldown[0][1] == time:
                freq, available_time = cooldown.popleft()
                heapq.heappush(heap, -freq)

            if heap:
                freq = - heapq.heappop(heap)
                freq -= 1

                if freq > 0:
                    cooldown.append((freq, time + n + 1))
            
            time += 1

        return time
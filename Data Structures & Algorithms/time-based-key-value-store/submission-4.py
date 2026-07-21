class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]

        if not values:
            return ""

        start = 0
        end = len(values) - 1
        answer = ""

        while start <= end:
            mid = (start + end)//2

            if values[mid][1] <= timestamp:
                answer = values[mid][0]
                start = mid + 1

            else:
                end = mid - 1

        return answer

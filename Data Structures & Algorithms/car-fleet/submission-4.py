class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda car:car[0], reverse=True)
        fleet = 0
        last_fleet_time = 0
        for position, speed in cars:
            time = (target - position) / speed
            if last_fleet_time == 0 or time > last_fleet_time:
                fleet += 1
                last_fleet_time = time

        return fleet
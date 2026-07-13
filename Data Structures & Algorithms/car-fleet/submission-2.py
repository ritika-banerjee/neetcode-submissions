class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0  
        stack = []
        cars = list(zip(position, speed))
        cars.sort(key=lambda car:car[0], reverse=True)

        for position, speed in cars:
            time = (target-position)/speed

            if not stack or time > stack[-1]:
                fleet += 1
                stack.append(time)

        return fleet
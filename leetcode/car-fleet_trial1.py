class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p, s in zip(position, speed):
            time = (target - p) / s
            cars.append((p, time))
        cars.sort(reverse=True)
        fleets = 0
        max_time = 0
        for p, t in cars:
            if t > max_time:
                fleets += 1
                max_time = t
        return fleets
        
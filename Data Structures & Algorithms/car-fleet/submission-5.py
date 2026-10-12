class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def math_thing(p, s):
            return (target - p) / s
        stack = []
        cars = sorted(zip(position, speed), reverse = True)
        for pos, spd in cars:
            if stack and math_thing(stack[-1][0], stack[-1][-1]) >= math_thing(pos, spd):
                continue
            stack.append((pos, spd))

        return len(stack)
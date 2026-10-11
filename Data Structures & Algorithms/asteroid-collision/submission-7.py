class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            exploded = False
            while stack and stack[-1] > 0 and a < 0:
                if abs(a) == stack[-1]:
                    exploded = True
                    stack.pop()
                    break
                elif abs(a) < stack[-1]:
                    exploded = True
                    break
                else:
                    stack.pop()
            if not exploded:
                stack.append(a)
        
        return stack
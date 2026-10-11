class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            exploded = False
            if not stack or stack[-1] < 0 or a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0:
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
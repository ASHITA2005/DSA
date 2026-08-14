class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        i = 0
        while i < n:
            asteroid = asteroids[i]
            if not stack or asteroid > 0 or (stack and stack[-1] < 0):
                stack.append(asteroid)
            else:
                flag = 0
                while stack and stack[-1] > 0 and stack[-1] <= abs(asteroid):
                    if stack[-1] == abs(asteroid):
                        flag = 1
                        stack.pop()
                        break
                    stack.pop()
                if (not flag and stack and stack[-1] <= abs(asteroid)) or (not flag and not stack):
                    stack.append(asteroid)
            i += 1
        return stack
                
                
                


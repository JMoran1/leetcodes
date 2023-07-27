"""
735. Asteroid Collision
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, 
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""


class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(x):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(x)
                elif stack[-1] == abs(x):
                    stack.pop()
        return stack


# Testcases
s = Solution()
print(s.asteroidCollision([5,10,-5]))
print(s.asteroidCollision([5,-5]))
print(s.asteroidCollision([10,2,-5]))


# Runtime: 104ms, faster than 87.7% of Python3 submissions
# Memory Usage: 17.46 MB, beats 77.71% of Python3 submissions
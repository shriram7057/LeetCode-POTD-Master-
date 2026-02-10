class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for a in asteroids:
            # Process collisions
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < -a:      # stack asteroid smaller → it explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a:   # both explode
                    stack.pop()
                break                    # incoming asteroid destroyed or both destroyed
            else:
                stack.append(a)          # no collision → safe

        return stack

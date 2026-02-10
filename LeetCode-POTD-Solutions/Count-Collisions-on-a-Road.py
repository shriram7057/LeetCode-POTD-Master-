1class Solution(object):
2    def countCollisions(self, directions):
3        stack = []
4        collisions = 0
5
6        for d in directions:
7            if d == 'R':
8                stack.append('R')
9            elif d == 'S':
10                while stack and stack[-1] == 'R':
11                    collisions += 1
12                    stack.pop()
13                stack.append('S')
14            else:  # d == 'L'
15                if not stack or stack[-1] == 'L':
16                    stack.append('L')
17                else:
18                    if stack[-1] == 'R':
19                        collisions += 2
20                        stack.pop()
21                        while stack and stack[-1] == 'R':
22                            collisions += 1
23                            stack.pop()
24                        stack.append('S')
25                    else:
26                        collisions += 1
27                        stack.append('S')
28
29        return collisions
30
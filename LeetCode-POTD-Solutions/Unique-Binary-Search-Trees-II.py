1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def generateTrees(self, n: int):
10        if n == 0:
11            return []
12
13        def build(start, end):
14            if start > end:
15                return [None]
16
17            trees = []
18            for root in range(start, end + 1):
19                leftTrees = build(start, root - 1)
20                rightTrees = build(root + 1, end)
21
22                for left in leftTrees:
23                    for right in rightTrees:
24                        node = TreeNode(root)
25                        node.left = left
26                        node.right = right
27                        trees.append(node)
28
29            return trees
30
31        return build(1, n)
32
class Solution(object):
    def isSymmetric(self, root):
        def isMirror(a, b):
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return isMirror(a.left, b.right) and isMirror(a.right, b.left)
        return isMirror(root.left, root.right) if root else True

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """

        def getLeaves(node, leaves):
            if not node:
                return
            if not node.left and not node.right:   # leaf node
                leaves.append(node.val)
                return
            getLeaves(node.left, leaves)
            getLeaves(node.right, leaves)

        leaves1 = []
        leaves2 = []

        getLeaves(root1, leaves1)
        getLeaves(root2, leaves2)

        return leaves1 == leaves2

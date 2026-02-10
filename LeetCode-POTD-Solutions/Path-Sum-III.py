class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        from collections import defaultdict
        
        prefix = defaultdict(int)
        prefix[0] = 1   # empty prefix

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val
            count = prefix[curr_sum - targetSum]   # number of valid paths ending here

            prefix[curr_sum] += 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix[curr_sum] -= 1   # backtrack

            return count

        return dfs(root, 0)

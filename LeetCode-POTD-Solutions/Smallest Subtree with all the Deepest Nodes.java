class Solution {
    public TreeNode subtreeWithAllDeepest(TreeNode root) {
        return dfs(root).node;
    }

    private Pair dfs(TreeNode node) {
        if (node == null) return new Pair(null, 0);

        Pair left = dfs(node.left);
        Pair right = dfs(node.right);

        if (left.depth > right.depth) return new Pair(left.node, left.depth + 1);
        if (left.depth < right.depth) return new Pair(right.node, right.depth + 1);
        return new Pair(node, left.depth + 1);
    }

    private static class Pair {
        TreeNode node;
        int depth;

        Pair(TreeNode n, int d) {
            node = n;
            depth = d;
        }
    }
}

class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;

        int left = heightLeft(root);
        int right = heightRight(root);

        if (left == right) return (1 << left) - 1;

        return 1 + countNodes(root.left) + countNodes(root.right);
    }

    private int heightLeft(TreeNode node) {
        int h = 0;
        while (node != null) {
            h++;
            node = node.left;
        }
        return h;
    }

    private int heightRight(TreeNode node) {
        int h = 0;
        while (node != null) {
            h++;
            node = node.right;
        }
        return h;
    }
}

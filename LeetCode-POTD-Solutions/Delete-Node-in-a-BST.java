class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;

        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } 
        else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } 
        else {
            // Node found

            // Case 1: No left child
            if (root.left == null) return root.right;

            // Case 2: No right child
            if (root.right == null) return root.left;

            // Case 3: Both children -> find inorder successor
            TreeNode cur = root.right;
            while (cur.left != null) {
                cur = cur.left;
            }

            root.val = cur.val;  // Replace value
            root.right = deleteNode(root.right, cur.val); // Delete successor
        }

        return root;
    }
}

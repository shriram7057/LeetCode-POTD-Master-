class Solution {
public:
    int dfs(TreeNode* node, int current) {
        if (!node) return 0;
        
        // Build the binary number
        current = (current << 1) | node->val;
        
        // If it's a leaf node, return the number
        if (!node->left && !node->right)
            return current;
        
        // Otherwise, sum from left and right subtrees
        return dfs(node->left, current) + dfs(node->right, current);
    }
    
    int sumRootToLeaf(TreeNode* root) {
        return dfs(root, 0);
    }
};
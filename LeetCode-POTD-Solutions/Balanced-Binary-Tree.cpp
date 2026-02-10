1class Solution {
2public:
3    int height(TreeNode* root) {
4        if (!root) return 0;
5
6        int leftHeight = height(root->left);
7        if (leftHeight == -1) return -1;
8
9        int rightHeight = height(root->right);
10        if (rightHeight == -1) return -1;
11
12        if (abs(leftHeight - rightHeight) > 1) return -1;
13
14        return 1 + max(leftHeight, rightHeight);
15    }
16
17    bool isBalanced(TreeNode* root) {
18        return height(root) != -1;
19    }
20};
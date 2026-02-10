1class Solution {
2public:
3    vector<TreeNode*> nodes;
4
5    void inorder(TreeNode* root) {
6        if (!root) return;
7        inorder(root->left);
8        nodes.push_back(root);
9        inorder(root->right);
10    }
11
12    TreeNode* build(int left, int right) {
13        if (left > right) return nullptr;
14
15        int mid = left + (right - left) / 2;
16        TreeNode* root = nodes[mid];
17
18        root->left = build(left, mid - 1);
19        root->right = build(mid + 1, right);
20
21        return root;
22    }
23
24    TreeNode* balanceBST(TreeNode* root) {
25        inorder(root);
26        return build(0, nodes.size() - 1);
27    }
28};
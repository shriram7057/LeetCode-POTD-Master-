1class Solution {
2public:
3    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
4        unordered_map<TreeNode*, TreeNode*> parent;
5        buildParent(root, nullptr, parent);
6
7        queue<TreeNode*> q;
8        unordered_set<TreeNode*> visited;
9
10        q.push(target);
11        visited.insert(target);
12
13        int dist = 0;
14
15        while (!q.empty()) {
16            int size = q.size();
17
18            if (dist == k) {
19                vector<int> result;
20                while (!q.empty()) {
21                    result.push_back(q.front()->val);
22                    q.pop();
23                }
24                return result;
25            }
26
27            while (size--) {
28                TreeNode* node = q.front();
29                q.pop();
30
31                if (node->left && !visited.count(node->left)) {
32                    visited.insert(node->left);
33                    q.push(node->left);
34                }
35
36                if (node->right && !visited.count(node->right)) {
37                    visited.insert(node->right);
38                    q.push(node->right);
39                }
40
41                if (parent[node] && !visited.count(parent[node])) {
42                    visited.insert(parent[node]);
43                    q.push(parent[node]);
44                }
45            }
46
47            dist++;
48        }
49
50        return {};
51    }
52
53private:
54    void buildParent(TreeNode* node, TreeNode* par,
55                     unordered_map<TreeNode*, TreeNode*>& parent) {
56        if (!node) return;
57        parent[node] = par;
58        buildParent(node->left, node, parent);
59        buildParent(node->right, node, parent);
60    }
61};
62
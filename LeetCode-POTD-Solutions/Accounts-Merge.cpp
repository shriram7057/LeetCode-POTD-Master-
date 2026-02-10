1class Solution {
2public:
3    unordered_map<string, string> parent;
4
5    string find(string x) {
6        if (parent[x] != x)
7            parent[x] = find(parent[x]);
8        return parent[x];
9    }
10
11    void unite(string a, string b) {
12        string pa = find(a);
13        string pb = find(b);
14        if (pa != pb)
15            parent[pb] = pa;
16    }
17
18    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
19        unordered_map<string, string> emailToName;
20
21        // 1️⃣ Initialize DSU
22        for (auto& acc : accounts) {
23            string name = acc[0];
24            for (int i = 1; i < acc.size(); i++) {
25                string email = acc[i];
26                if (!parent.count(email))
27                    parent[email] = email;
28                emailToName[email] = name;
29            }
30        }
31
32        // 2️⃣ Union emails within same account
33        for (auto& acc : accounts) {
34            string firstEmail = acc[1];
35            for (int i = 2; i < acc.size(); i++) {
36                unite(firstEmail, acc[i]);
37            }
38        }
39
40        // 3️⃣ Group emails by root
41        unordered_map<string, vector<string>> groups;
42        for (auto& [email, _] : parent) {
43            groups[find(email)].push_back(email);
44        }
45
46        // 4️⃣ Build result
47        vector<vector<string>> res;
48        for (auto& [root, emails] : groups) {
49            sort(emails.begin(), emails.end());
50            vector<string> account;
51            account.push_back(emailToName[root]);
52            account.insert(account.end(), emails.begin(), emails.end());
53            res.push_back(account);
54        }
55
56        return res;
57    }
58};
59
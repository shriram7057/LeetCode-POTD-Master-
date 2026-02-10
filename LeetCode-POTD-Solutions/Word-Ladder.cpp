1class Solution {
2public:
3    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
4        unordered_set<string> dict(wordList.begin(), wordList.end());
5        
6        // If endWord is not in the dictionary, no solution
7        if (!dict.count(endWord)) return 0;
8        
9        queue<string> q;
10        q.push(beginWord);
11        
12        int level = 1;  // beginWord counts as level 1
13        
14        while (!q.empty()) {
15            int size = q.size();
16            while (size--) {
17                string word = q.front();
18                q.pop();
19                
20                // Try changing each character
21                for (int i = 0; i < word.size(); i++) {
22                    char original = word[i];
23                    
24                    for (char c = 'a'; c <= 'z'; c++) {
25                        if (c == original) continue;
26                        word[i] = c;
27                        
28                        if (word == endWord) {
29                            return level + 1;
30                        }
31                        
32                        if (dict.count(word)) {
33                            q.push(word);
34                            dict.erase(word);  // mark as visited
35                        }
36                    }
37                    
38                    word[i] = original;  // restore
39                }
40            }
41            level++;
42        }
43        
44        return 0;
45    }
46};
47
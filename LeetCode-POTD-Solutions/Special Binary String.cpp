class Solution {
public:
    string makeLargestSpecial(string s) {
        vector<string> subs;
        int count = 0, start = 0;
        
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '1') count++;
            else count--;
            
            // Found a special substring
            if (count == 0) {
                // Recursively process inside
                string inner = makeLargestSpecial(s.substr(start + 1, i - start - 1));
                subs.push_back("1" + inner + "0");
                start = i + 1;
            }
        }
        
        // Sort in descending lexicographical order
        sort(subs.begin(), subs.end(), greater<string>());
        
        string result;
        for (string &sub : subs)
            result += sub;
            
        return result;
    }
};
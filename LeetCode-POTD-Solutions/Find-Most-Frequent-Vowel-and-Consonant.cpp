class Solution {
public:
    int maxFreqSum(string s) {
        unordered_map<char, int> freq;
        for (char c : s) {
            if (isalpha(c)) freq[tolower(c)]++;
        }
        
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        
        int maxVowel = 0, maxConsonant = 0;
        for (auto& p : freq) {
            if (isVowel(p.first))
                maxVowel = max(maxVowel, p.second);
            else
                maxConsonant = max(maxConsonant, p.second);
        }
        
        return maxVowel + maxConsonant;
    }
};

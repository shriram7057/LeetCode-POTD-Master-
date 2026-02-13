class Solution {
    int f(char x, char y, char z, const string& s, const int n){
        int maxi = 0;
        int i = 0;
        while(i<n){
            if(s[i] == z) {
                i++;
                continue;
            }

            unordered_map<int,int>mp;
            int cnt = 0;
            mp[cnt] = i;
            int j = i;
            while(j<n && s[j] != z){
                cnt += (s[j] == x)? -1: 1;
                if(mp.count(cnt)){
                    maxi = max(maxi, j-mp[cnt]+1);
                }
                else{
                    mp[cnt] = j+1;
                }
                j++;
            }
            i=j;
        }

        return maxi;
    }

public:
    int longestBalanced(string s) {
        int n = s.size();
        int maxi = 0;

        // for single character
        int i=0;
        while(i<n){
            int j = i;
            int cnt = 0;
            while(j<n && s[j] == s[i]){
                cnt++;
                j++;
            }
            maxi = max(maxi, cnt);
            i=j;
        }

        // finding max for 2 characters
        maxi = max(maxi, f('a', 'b', 'c', s, n));
        maxi = max(maxi, f('b', 'c', 'a', s, n));
        maxi = max(maxi, f('a', 'c', 'b', s, n));

        // finding max for considering all 3 character
        map<pair<int,int>, int>mp;
        int ca = 0, cb = 0, cc = 0;
        mp[{0, 0}] = -1;
        for(int i=0; i<n; i++){
            if(s[i] == 'a') ca++;
            else if(s[i] == 'b') cb++;
            else cc++;
            if(mp.count({ca-cb, cb-cc})){
                maxi = max(maxi, i-mp[{ca-cb, cb-cc}]);
            }   
            else {
                mp[{ca-cb, cb-cc}] = i;
            }
        }

        return maxi;
    }
};
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        int totalTime = 0;
        int n = colors.size();

        for (int i = 1; i < n; i++) {
            if (colors[i] == colors[i - 1]) {
                // Remove the one with smaller time
                totalTime += min(neededTime[i], neededTime[i - 1]);
                // Keep the one with larger time for next comparison
                neededTime[i] = max(neededTime[i], neededTime[i - 1]);
            }
        }

        return totalTime;
    }
};

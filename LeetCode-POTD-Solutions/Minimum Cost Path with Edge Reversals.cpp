#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int,int>>> g(n);
        
        // Normal edges
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            g[u].push_back({v, w});
        }
        
        // Add reversible edges (incoming reversed with cost 2*w)
        vector<vector<pair<int,int>>> incoming(n);
        for (auto &e : edges) {
            incoming[e[1]].push_back({e[0], e[2]});
        }
        
        const long long INF = LLONG_MAX / 4;
        vector<long long> dist(n, INF);
        priority_queue<pair<long long,int>, vector<pair<long long,int>>, greater<pair<long long,int>>> pq;
        
        dist[0] = 0;
        pq.push({0, 0});
        
        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();
            if (d > dist[u]) continue;
            if (u == n - 1) return (int)d;
            
            // Normal outgoing edges
            for (auto &[v, w] : g[u]) {
                if (dist[v] > d + w) {
                    dist[v] = d + w;
                    pq.push({dist[v], v});
                }
            }
            
            // Reverse one incoming edge at cost 2*w
            for (auto &[v, w] : incoming[u]) {
                long long nd = d + 2LL * w;
                if (dist[v] > nd) {
                    dist[v] = nd;
                    pq.push({nd, v});
                }
            }
        }
        
        return -1;
    }
};

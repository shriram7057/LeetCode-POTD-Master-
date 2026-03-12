class DSU {
public:
    vector<int> p, r;
    DSU(int n) {
        p.resize(n);
        r.resize(n,0);
        for(int i=0;i<n;i++) p[i]=i;
    }
    
    int find(int x){
        if(p[x]==x) return x;
        return p[x]=find(p[x]);
    }
    
    bool unite(int a,int b){
        a=find(a); b=find(b);
        if(a==b) return false;
        if(r[a]<r[b]) swap(a,b);
        p[b]=a;
        if(r[a]==r[b]) r[a]++;
        return true;
    }
};

class Solution {
public:
    
    bool can(int n, vector<vector<int>>& edges, int k, int X){
        DSU dsu(n);
        int used=0;
        int upgrades=0;
        
        vector<vector<int>> freeEdges;
        vector<vector<int>> upEdges;
        
        for(auto &e:edges){
            int u=e[0], v=e[1], s=e[2], must=e[3];
            
            if(must){
                if(s<X) return false;
                if(!dsu.unite(u,v)) return false;
                used++;
            }else{
                if(s>=X) freeEdges.push_back(e);
                else if(2*s>=X) upEdges.push_back(e);
            }
        }
        
        for(auto &e:freeEdges){
            if(dsu.unite(e[0],e[1])) used++;
        }
        
        for(auto &e:upEdges){
            if(used==n-1) break;
            if(dsu.unite(e[0],e[1])){
                upgrades++;
                used++;
                if(upgrades>k) return false;
            }
        }
        
        return used==n-1;
    }
    
    int maxStability(int n, vector<vector<int>>& edges, int k) {
        
        int lo=1, hi=200000;
        int ans=-1;
        
        while(lo<=hi){
            int mid=(lo+hi)/2;
            
            if(can(n,edges,k,mid)){
                ans=mid;
                lo=mid+1;
            }else{
                hi=mid-1;
            }
        }
        
        return ans;
    }
};
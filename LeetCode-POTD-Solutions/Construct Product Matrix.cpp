class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        const int MOD = 12345;
        int n = grid.size(), m = grid[0].size();
        int N = n * m;

        vector<int> arr(N), prefix(N, 1), suffix(N, 1);

        // flatten
        int k = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                arr[k++] = grid[i][j] % MOD;

        // prefix products
        for (int i = 1; i < N; i++)
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD;

        // suffix products
        for (int i = N - 2; i >= 0; i--)
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD;

        // result
        vector<vector<int>> res(n, vector<int>(m));
        k = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                res[i][j] = (prefix[k] * suffix[k]) % MOD;
                k++;
            }
        }

        return res;
    }
};
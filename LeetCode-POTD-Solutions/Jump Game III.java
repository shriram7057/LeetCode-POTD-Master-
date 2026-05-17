class Solution {
    public boolean canReach(int[] arr, int start) {
        boolean[] visited = new boolean[arr.length];
        return dfs(arr, start, visited);
    }

    private boolean dfs(int[] arr, int idx, boolean[] visited) {
        // Out of bounds or already visited
        if (idx < 0 || idx >= arr.length || visited[idx]) {
            return false;
        }

        // Found a zero
        if (arr[idx] == 0) {
            return true;
        }

        visited[idx] = true;

        // Jump forward or backward
        return dfs(arr, idx + arr[idx], visited) ||
               dfs(arr, idx - arr[idx], visited);
    }
}
1class Solution {
2    public int maximalRectangle(char[][] matrix) {
3        if (matrix.length == 0) return 0;
4
5        int rows = matrix.length, cols = matrix[0].length;
6        int[] heights = new int[cols];
7        int maxArea = 0;
8
9        for (int i = 0; i < rows; i++) {
10            for (int j = 0; j < cols; j++) {
11                heights[j] = matrix[i][j] == '1' ? heights[j] + 1 : 0;
12            }
13            maxArea = Math.max(maxArea, largestRectangleArea(heights));
14        }
15        return maxArea;
16    }
17
18    private int largestRectangleArea(int[] heights) {
19        java.util.Stack<Integer> stack = new java.util.Stack<>();
20        int max = 0;
21
22        for (int i = 0; i <= heights.length; i++) {
23            int h = (i == heights.length) ? 0 : heights[i];
24            while (!stack.isEmpty() && h < heights[stack.peek()]) {
25                int height = heights[stack.pop()];
26                int width = stack.isEmpty() ? i : i - stack.peek() - 1;
27                max = Math.max(max, height * width);
28            }
29            stack.push(i);
30        }
31        return max;
32    }
33}
34
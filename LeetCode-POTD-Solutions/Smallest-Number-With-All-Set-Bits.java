class Solution {
    static int smallestNumber(int n) {
        int x = 1;
        while (x < n) {
            x = (x << 1) | 1;  // multiply by 2 and set last bit to 1
        }
        return x;
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println(smallestNumber(n)); // Output: 15
    }
}

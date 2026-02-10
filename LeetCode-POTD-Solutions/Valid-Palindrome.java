class Solution {
    public boolean isPalindrome(String s) {
        // Step 1: Remove non-alphanumeric characters and convert to lowercase
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

        // Step 2: Use two pointers (start and end)
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false; // mismatch found
            }
            left++;
            right--;
        }

        return true; // no mismatches found
    }
}

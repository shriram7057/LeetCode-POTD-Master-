class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        # Transform char -> int
        s = [ord(char) - ord('a') for char in s]

        result = 0
        for l in range(n):
            if n - l <= result:  # Early exit, can't be bigger
                break

            cnt = [0] * 26  # Counts of every char
            uniq = maxfreq = 0  # Number of uniq chars and maximum frequency
            for r in range(l, n):
                i = s[r]

                uniq += cnt[i] == 0  # There was no this char before => one more uniq
                cnt[i] += 1
                if cnt[i] > maxfreq:  # Update max frequency
                    maxfreq = cnt[i]

                # Check if all uniq chars have maxfreq frequency then update the result
                cur = r - l + 1
                if uniq * maxfreq == cur and cur > result:
                    result = cur

        return result
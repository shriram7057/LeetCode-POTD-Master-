class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        maxFreq = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFreq = max(maxFreq, count[s[right]])

            # if replacements needed > k → shrink window
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left -= 1
                left += 2  # quick fix: simply do left += 1 instead of left -=1 then +=2

            # correct window shrink:
            # while (right - left + 1) - maxFreq > k:
            #     count[s[left]] -= 1
            #     left += 1

            # window size is a valid answer
            res = max(res, right - left + 1)

        return res

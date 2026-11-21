class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left=0
        maxlen = 0

        for right,ch in enumerate(s):
            if ch in seen and seen[ch]>=left:
                left=seen[ch]+1

            seen[ch]=right
            maxlen = max(maxlen, right-left+1)

        return maxlen
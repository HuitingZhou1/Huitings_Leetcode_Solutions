class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, maxl = 0, 0
        count = {}

        for i,c in enumerate(s):
            count[c] = 1+count.get(c,0)
            while count[c]>1:
                count[s[left]] -= 1
                left += 1
            maxl = max(i - left +1, maxl)

        return maxl

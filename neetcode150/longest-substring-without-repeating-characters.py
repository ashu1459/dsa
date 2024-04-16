class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        left, right, longestSubStr = 0, 1, 1
        # maps = list(s)

        # while right < len(s):
        #     if s[right] in maps[left:right]:
        #         left = maps[left:right].index(s[right]) + left + 1
        #     else:
        #         longestSubStr = max(longestSubStr, right - left + 1)
        #     right += 1

        # solution-2 using O(n) time and space
        hashset = set()
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1

            hashset.add(s[right])
            longestSubStr = max(longestSubStr, right - left + 1)

        return longestSubStr
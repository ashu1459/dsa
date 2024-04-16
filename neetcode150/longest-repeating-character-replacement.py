class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longestStr = 0
        hashmap = {}

        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right], 0)

            while (right - left + 1) - max(hashmap.values()) > k:
                hashmap[s[left]] -= 1
                left += 1

            longestStr = max(longestStr, right - left + 1)

        return longestStr

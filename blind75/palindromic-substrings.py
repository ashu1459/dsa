class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ans = 0

        def countPal(l, r):
            res = 0
            while l >= 0 and r < N and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(N):
            # odd case: like bab
            ans += countPal(i, i)

            # even case: like baac
            ans += countPal(i, i + 1)
        
        return ans
        
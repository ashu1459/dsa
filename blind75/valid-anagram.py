class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        # Soluton-1 -- O(n) -- we consider sorting time complexity to be O(nlogn) and space to be O(1)
        # s_l = list(s)
        # t_l = list(t)
        
        # s_l.sort()
        # t_l.sort()

        # if s_l == t_l:
        #     return True 

        # return False

        # Solution-2 Time - O(n), Space - O(s+t)
        sCount, tCount = {}, {}

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        
        for charac in sCount:
            if sCount[charac] != tCount.get(charac, 0):
                return False

        return True
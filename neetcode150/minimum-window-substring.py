class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # t_count = {}
        # s_count = {}
        # min_str = ''
        # left_indexes = []
        # continue_iteration = False

        # for i in range(len(t)):
        #     t_count[t[i]] = 1 + t_count.get(t[i], 0)

        # for r in range(len(s)):
        #     if s[r] in t_count:
        #         if len(left_indexes) == 0:
        #             left = r

        #         s_count[s[r]] = 1 + s_count.get(s[r], 0)

        #         if s_count[s[r]] >= t_count[s[r]]:
        #             left_indexes.append(r)
                
        #         # if s_count[s[r]] > t_count[s[r]]:
        #         #     # print(r, t_count, s_count, left_indexes)
        #         #     # s_count[s[r]] -= 1
        #         #     s_count[s[left_indexes[0]]] -= 1
        #         #     left = left_indexes[1]
        #         #     left_indexes = left_indexes[1:]
                
        #         if len(t_count) == len(s_count):
        #             for i in t_count:
        #                 if s_count[i] >= t_count[i]:
        #                     continue
        #                 continue_iteration = True
        #                 break
                
        #         if continue_iteration:
        #             continue_iteration = False
        #             continue

        #         # if t_count == s_count:
        #         if len(min_str) == 0 or len(s[left:r + 1]) < len(min_str):
        #             min_str = s[left:r + 1]
                
        #         s_count[s[left]] -= 1

        #         if len(left_indexes) > 1:
        #             left = left_indexes[1]
        #             left_indexes = left_indexes[1:]

        # return min_str

        # Soluion-2 O(n)
        # if t == "":
        #     return ""

        # countT = {}
        # window = {}

        # for c in t:
        #     countT[c] = 1 + countT.get(c, 0)
        
        # have, need = 0, len(countT)
        # res, resLen = [-1,-1], float("infinity")
        # l = 0

        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] = 1 + window.get(c, 0)
            
        #     if c in countT and window[c] == countT[c]:
        #         have += 1

        #     while have == need:
        #         if (r - l + 1) < resLen:
        #             res = [l, r]
        #             resLen = r - l + 1
                
        #         window[s[l]] -= 1

        #         if s[l] in countT and window[s[l]] < countT[s[l]]:
        #             have -= 1
        #         l += 1

        # left, right = res

        # return s[left:right + 1] if resLen != float("infinity") else ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        l, strLen = 0, float("infinity")
        res, window = [-1, -1], {}

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while need == have:
                if (r - l + 1) < strLen:
                    strLen = r - l + 1
                    res = [l, r]

                window[s[l]] -= 1
                
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        left, right = res

        return s[left:right + 1] if strLen != float("infinity") else ""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Solution - 1 using sorting, O(n.nlogn)
        # s1 = ''.join(sorted(s1))
        # left = 0
        # s1_len = len(s1)
        # right = left + s1_len - 1

        # while right < len(s2):
        #     if s1 == ''.join(sorted(s2[left:right+1])):
        #         return True
            
        #     left += 1
        #     right += 1
            
        # return False

        # solution-2 : without sorting O(n)
        if len(s2) < len(s1): return False
        # s1_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, }
        # chr(97) is 'a' and chr(122) is 'z' produces dict like above
        s1_count = dict((chr(i), 0) for i in range(97, 123))
        s2_count = dict((chr(i), 0) for i in range(97, 123))

        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1

        if s1_count == s2_count:
            return True

        matches = 0
        left = 0

        for right in range(len(s1), len(s2)):
            s2_count[s2[right]] += 1
            s2_count[s2[left]] -= 1

            if s1_count == s2_count:
                return True
            
            left += 1

        return False




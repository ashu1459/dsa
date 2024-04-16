class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) < 2:
            return True

        s = s.lower()

        # Solution-1: using exrtra memory and built-in method isalnum()
        # new_s = ''

        # for string in s:
        #     if string.isalnum():
        #         new_s += string

        # new_s_len = len(new_s)

        # if new_s_len < 2:
        #     return True
        
        # for i in range(new_s_len//2):
        #     if new_s[i] != new_s[new_s_len-1-i]:
        #         return False

        # Solution-2:
        l_pointer = 0
        r_pointer = len(s)-1

        while l_pointer < r_pointer:
            if self.isAlphaNum(s[l_pointer]):
                if self.isAlphaNum(s[r_pointer]):
                    if s[l_pointer] == s[r_pointer]:
                        l_pointer += 1
                        r_pointer -= 1
                    else:
                        return False
                else:
                    r_pointer -= 1
            else:
                l_pointer += 1

        return True

    def isAlphaNum(self, c):
        return 48 <= ord(c) <= 57 or 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122
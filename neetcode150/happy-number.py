class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        def getSquaredAddition(n):
            output = 0
            while n:
                digit = n % 10
                output += digit**2
                n = n // 10
            return output

        while n not in hashset:
            hashset.add(n)
            n = getSquaredAddition(n)

            if n == 1:
                return True
        
        return False
        
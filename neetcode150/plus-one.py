class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        # prev = 0

        # for i in range(N):
        #     prev += digits[N - 1 - i] * (10**i)

        # prev += 1

        # return [int(i) for i in str(prev)]


        # Solution-2: aster and TC - O(n)
        digits = digits[::-1]
        one, i = 1, 0
        
        while one:
            if i < N:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        
        return digits[::-1]
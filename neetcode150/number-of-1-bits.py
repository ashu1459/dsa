class Solution:
    def hammingWeight(self, n: int) -> int:
        # nums = str(bin(n))
        # res = 0
        # for n in nums:
        #     if n == '1':
        #         res += 1
        # return res

        # res = 0
        # while n:
        #     n = n & (n-1)
        #     res += 1
        # return res

        # Bit shifting
        res = 0
        while n:
            res += n % 2
            n = n >> 1 # shift the bit to the right by 1
        return res
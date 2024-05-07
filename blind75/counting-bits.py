class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for i in range(n + 1):
            num = str(bin(i).replace('0b', ''))
            res.append(num.count('1'))

        return res
class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = True if n < 0 else False

        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            res = helper(x * x, n // 2)
            # res = res * res # instead of this, we are writing x * x in above line
            return (x * res) if n % 2 else res
        
        ans = helper(x, abs(n))

        return (1 / ans) if negative else ans
        
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        N1, N2 = len(num1), len(num2)

        ans = [0] * (N1 + N2)
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(N1):
            for j in range(N2):
                # subtracting from '0' to obtain ASCII difference (51 - 48 = 3)
                int_n1 = ord(num1[i]) - ord('0')
                int_n2 = ord(num2[j]) - ord('0')

                product = (int_n1 * int_n2)
                
                ans[i + j] += product
                ans[i + j + 1] += ans[i + j] // 10
                ans[i + j] = ans[i + j] % 10
        
        ans, begin = ans[::-1], 0
        # removing any prefix zeros
        while begin < len(ans) and ans[begin] == 0:
            begin += 1

        return ''.join(map(str, ans[begin:]))
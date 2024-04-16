class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # solution-1 Brute force
        # res = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     j = i + 1

        #     while j < len(temperatures):
        #         if temperatures[i] < temperatures[j]:
        #             res[i] = j - i
        #             break
        #         j += 1

        # return res

        # O(n) solution
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)-1, -1, -1):
            while stack:
                # bigger temperature found, calculate the distance(index difference)
                if temperatures[i] < temperatures[stack[-1]]:
                    res[i] = stack[-1] - i
                    break
                else:
                    # keep poping until we find a bigger temperature
                    stack.pop()
            stack.append(i)
        
        return res

        # answer = [0] * len(temperatures)
        # stack = []
        # for r in range(len(temperatures)):
        #     while stack and temperatures[stack[-1]] < temperatures[r]:
        #         l = stack.pop()
        #         answer[l] = r-l

        #     stack.append(r)

        return answer

            


class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) < 3:
            return 0

    # solution - 1
    #     stack = []
    #     collected = 0
    #     l, r = 0, 1

    #     while r < len(height):
    #         if height[l] == 0:
    #             l += 1
    #             r += 1
    #             continue

    #         if height[r] <= height[r-1]:
    #             stack.append(height[l] - height[r])
    #             r += 1
    #         else:
    #             if height[r] >= height[l]:
    #                 r += 1
    #                 l = r - 1
    #                 stack, collected = self.calculateWater(stack, collected, 0)
    #             else:
    #                 toLeave = height[l] - height[r]
    #                 stack, collected = self.calculateWater(stack, collected, toLeave)
    #                 stack.append(height[l] - height[r])
    #                 r += 1

    #     return collected

    # def calculateWater(self, stack, collected, toLeave):
    #     for i, num in enumerate(stack):
    #         if num > toLeave:
    #             collected += (num - toLeave)
    #             stack[i] = toLeave

    #     if toLeave == 0:
    #         stack = []

    #     return stack, collected

        # solution-2: O(n) time, O(n) space
        # total_len = len(height)
        # left_max = 0
        # right_max = 0
        # left = [0] * total_len
        # right = [0] * total_len

        # res = 0

        # for i in range(total_len):
        #     left_max = max(left_max, height[i])
        #     left[i] = left_max

        #     right_max = max(right_max, height[total_len - (i+1)])
        #     right[total_len - (i+1)] = right_max

        # for i, num in enumerate(height):
        #     res += (min(left[i], right[i]) - num)

        # return res

        # solution-3: O(n) time, O(1) space
        res = 0
        total_len = len(height)

        l = 0
        r = total_len - 1
        i = 0
        max_left = height[l]
        max_right = height[r]

        while l < r:
            if l == i:
                max_left = max(max_left, height[i])
            else:
                max_right = max(max_right, height[i])

            holding = min(max_left, max_right) - height[i]
            if holding > 0:
                res += holding

            if max_right < max_left:
                i = r - 1
                r -= 1
            else:
                i = l + 1
                l += 1

        return res

        


        
        
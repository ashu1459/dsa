class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute force solution
        # max_h = 0
        # for i, h1 in enumerate(heights):
        #     counter = h1
        #     j = 0
        #     while j < len(heights) and heights[j] != 0 and (j <= i or heights[i] <= heights[j]):
        #         if i == j: continue
        #         if heights[i] <= heights[j]:
        #             counter += heights[i]
        #         j += 1
        #     max_h = max(max_h, counter)
        
        # return max_h

        # solution-2: O(n) time and space
        maxArea = 0
        stack = [] # pair (index, height)

        for i, h in enumerate(heights):
            index = i
            # pop each bigger elem on left and calculate maxArea
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
            
            stack.append([index,h])
        
        # for i, h in stack:
        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea
        
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        maximum = 0

        while left < right:
            current_max = min(height[left], height[right]) * (right - left)
            maximum = max(maximum, current_max)

            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1

        return maximum





        
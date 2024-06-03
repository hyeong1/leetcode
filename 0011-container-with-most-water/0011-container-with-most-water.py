class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        low, high = 0, len(height)-1

        while low != high:
            max_water = max(max_water, min(height[low], height[high]) * (high - low))
            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1

        return max_water
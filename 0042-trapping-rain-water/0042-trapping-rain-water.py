class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(height)):
            if stack and height[stack[-1]] < height[i]:
                pre = stack.pop()
                while stack and height[stack[-1]] <= height[i]:
                    h = stack.pop()
                    if height[h] == height[pre]:
                        continue
                    ans += (height[h] - height[pre]) * (i - h - 1)
                    pre = h
                if stack:
                    ans += (height[i] - height[pre]) * (i - stack[-1] - 1)
            stack.append(i)
        
        return ans     
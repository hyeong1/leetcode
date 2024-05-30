class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s2 = float('-inf')
        stack = []

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s2:
                return True
            while stack and nums[i] > stack[-1]:
                s2 = stack.pop()
            stack.append(nums[i])
        return False
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        left, right = 0, len(nums)-1
        
        while left <= right:
            if nums[left] == target:
                ans[0] = left
                break
            left += 1

        while right >= left:
            if nums[right] == target:
                ans[1] = right
                break
            right -= 1

        return ans
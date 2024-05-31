class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_len = float('inf')
        _sum = 0

        for end in range(len(nums)):
            _sum += nums[end]
            while _sum >= target:
                min_len = min(min_len, end-start+1)
                _sum -= nums[start]
                start += 1

        return 0 if min_len == float('inf') else min_len
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix = []
        mx = -inf

        for n in nums:
            mx = max(mx, n)
            prefix.append(max(mx-n, 0))
        print(prefix)
        
        suffix = []
        for n in reversed(nums):
            if not suffix:
                suffix.append(n)
            else:
                suffix.append(max(n, suffix[-1]))
        suffix[:] = reversed(suffix)
        print(suffix)

        _max = 0
        for i in range(1, len(nums)-1):
            _max = max(_max, prefix[i] * suffix[i+1])
        return _max
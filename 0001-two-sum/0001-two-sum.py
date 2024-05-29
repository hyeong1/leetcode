class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, n in enumerate(nums):
            n2 = target - n
            if n2 in nums_dict:
                return [nums_dict[n2], i]
            nums_dict[n] = i
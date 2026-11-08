class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_new = set(nums)
        if len(nums_new) == len(nums):
            return False
        else:
            return True
        
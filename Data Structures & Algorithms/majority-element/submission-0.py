class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = sorted(nums)
        return a[len(a)//2]
        
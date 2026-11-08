class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for ind,val in enumerate(nums):
            diff = target - val

            if diff in seen:
                return [seen[diff],ind]
            else:
                seen[val] = ind
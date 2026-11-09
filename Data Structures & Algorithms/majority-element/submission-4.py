class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #We could do it using the sorted() way and finding the middle element of the sorted list.
        #But we wanna do it using the Boyer Moore's method. Where we cancel the pairs and pick the one that is left. 
       # [1, 2, 1, 2, 2] Value = 1 2 1 2 2 


        element, count = None, 0

        for value in nums:
            if count == 0:
                element = value
            if element == value:
                count +=1
            else:
                count -= 1
        return element
        
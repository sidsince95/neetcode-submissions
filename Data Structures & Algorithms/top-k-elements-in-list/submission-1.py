class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0)+1
        ordered = sorted(seen, key = seen.get, reverse = True)
        return ordered[:k]

    
            

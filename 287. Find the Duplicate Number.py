class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {} 
        for item in nums: 
            if (item in freq): 
                freq[item] += 1
            else: 
                freq[item] = 1
        for f in freq:
            if freq[f]>=2:
                return f
        return -1
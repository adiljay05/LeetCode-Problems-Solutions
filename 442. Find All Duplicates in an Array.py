class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {} 
        dup = []
        for item in nums: 
            if (item in freq): 
                freq[item] += 1
            else: 
                freq[item] = 1
        for f in freq:
            if freq[f]>1:
                dup.append(f)
        return dup
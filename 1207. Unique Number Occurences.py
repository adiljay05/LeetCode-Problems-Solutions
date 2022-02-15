class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {} 
        for item in arr: 
            if (item in freq): 
                freq[item] += 1
            else: 
                freq[item] = 1
        if(len(set(freq.values()))<len(freq)):
            return False
        return True
        
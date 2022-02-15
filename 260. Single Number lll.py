class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {} 
        num = []
        for item in nums: 
            if (item in freq): 
                freq[item] += 1
            else: 
                freq[item] = 1
        for f in freq:
            if freq[f]==1:
                num.append(f)
            # print(f, freq[f])
        return num
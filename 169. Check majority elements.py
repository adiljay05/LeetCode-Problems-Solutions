class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        expected_size = int(len(nums)/2)
        dict_ = {}
        for n in nums:
            if n in dict_:
                dict_[n]+=1
            else:
                dict_[n]=1
        for d in dict_:
            if dict_[d]>expected_size:
                return d
        return -1
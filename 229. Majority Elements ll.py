class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        expected_size = int(len(nums)/3)
        dict_ = {}
        for n in nums:
            if n in dict_:
                dict_[n]+=1
            else:
                dict_[n]=1
        numbers = []
        for d in dict_:
            if dict_[d]>expected_size:
                numbers.append(d)
        return numbers
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s1 = set([*range(1,len(nums)+1)])
        nums = set(nums)
        print(s1)
        return s1-nums
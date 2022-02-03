class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ""
        for n in nums:
            s+=str(n)
        s=s.split('0')
        max_len = 0
        for s1 in s:
            if len(s1)>max_len:
                max_len=len(s1)
        return max_len
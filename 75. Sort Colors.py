class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = w = b = 0
        for n in nums:
            if n == 0:
                r+=1
            elif n == 1:
                w+=1
            else:
                b+=1
        nums.clear()
        while r>0:
            nums.append(0)
            r-=1
        while w>0:
            nums.append(1)
            w-=1
        while b>0:
            nums.append(2)
            b-=1
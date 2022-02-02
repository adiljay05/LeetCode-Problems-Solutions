class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i1 = 0
        power = 0 
        while power<=n:
            power = pow(2,i1)
            if power==n:
                return True
            i1+=1
        return False
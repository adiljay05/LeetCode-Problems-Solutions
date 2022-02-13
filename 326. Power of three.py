class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==2:
            return False
        elif n == 1:
            return True
        if n<1:
            return False
        ans = 1
        while ans<n:
            ans = ans * 3
            if ans == n:
                return True
        return False
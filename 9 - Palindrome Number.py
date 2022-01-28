class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        rev=0
        while(n>0):
            dig=n%10
            rev=rev*10+dig
            n=n//10
        if x == rev:
            return True
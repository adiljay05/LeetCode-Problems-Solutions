class Solution:
    def addDigits(self, num: int) -> int:
        n = num
        sum_ = 0
        while True:
            while n>0:
                sum_+=(n%10)
                n=n//10
                print(sum_)
            if sum_>9:
                n = sum_
                sum_ = 0
            else:
                break
        return sum_
            
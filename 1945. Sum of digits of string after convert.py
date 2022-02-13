class Solution:
    def getLucky(self, s: str, k: int) -> int:
        sum_ = 0
        string = ""
        for s1 in s:
            string+=str(ord(s1)-96)
        while k>0:
            # print(string)
            for st in string:
                sum_+=int(st)
            k-=1
            string = str(sum_)
            if k>0:
                sum_=0
        return sum_
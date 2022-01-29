class Solution:
    def reverse(self, x: int) -> int:
        rev = ""
        minus = False
        if x<0:
            minus = True
            x = abs(x)
        if x<10:
            return x
        i = x
        rev+=str(int(i%10))
        i=i/10
        while i>0:
            rev+=str(int(i%10))
            i=int(i/10)
        if minus:
            if 0-int(rev)<-2147483648:
                return 0
            return 0-int(rev)
        if int(rev)>2147483647:
            return 0
        return int(rev)
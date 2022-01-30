class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ""
        a = a[::-1]
        b = b[::-1]
        if len(a)<len(b):
            diff = len(b)-len(a)
            a = a + ('0'*diff)
        else:
            diff = len(a)-len(b)
            b = b + ('0'*diff)
        # print(a)
        # print(b)
        for i in range(len(a)):
            sum = int(a[i])+int(b[i])+carry
            if sum == 1:
                ans+=str(sum)
                carry = 0
            elif sum == 2:
                ans+='0'
                carry = 1
            elif sum == 3:
                ans+='1'
                carry = 1
            else:
                ans+='0'
                carry = 0
        if carry!=0:
            ans+='1'
        return ans[::-1]
                
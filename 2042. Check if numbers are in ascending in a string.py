class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(' ')
        dig = []
        for s1 in s:
            try:
                s2 = int(s1)
                dig.append(int(s1))
            except:
                pass
        dig1 = sorted(dig)
        for i in range(0,len(dig1)-1):
            if dig1[i]==dig1[i+1]:
                return False
        if dig == dig1:
            return True
        return False
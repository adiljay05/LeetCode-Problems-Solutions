class Solution(object):
    def checkString(self, s):
        s1 = sorted(s)
        s1 = ''.join(s1)
        # print(s1)
        if s == s1:
            return True
        return False
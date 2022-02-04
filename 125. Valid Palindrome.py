class Solution(object):
    def isPalindrome(self, s):
        if s.strip()=="":
            return True
        alphabets = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        string = ""
        for s1 in s:
            if alphabets.find(s1)>-1:
                string+=s1
        if string.lower()==string.lower()[::-1]:
            return True
        return False
        
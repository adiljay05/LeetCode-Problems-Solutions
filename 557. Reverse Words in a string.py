class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split(" ")
        new_string = ""
        for s1 in string:
            new_string+= s1[::-1]+" "
        return new_string.strip()
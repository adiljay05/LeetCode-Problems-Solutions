class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip().split(' ')
        return len(s1[len(s1)-1])
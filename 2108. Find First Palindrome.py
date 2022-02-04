class Solution(object):
    def firstPalindrome(self, words):
        for w in words:
            if w==w[::-1]:
                return w
        return ""
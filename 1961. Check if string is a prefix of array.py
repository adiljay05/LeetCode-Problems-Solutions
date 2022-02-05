class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        string = ""
        for w in words:
            string+=w
            if s==string:
                return True
        return False
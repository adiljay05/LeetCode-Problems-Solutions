class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        count = 0
        for t1 in text:
            flag = True
            for t in t1:
                if brokenLetters.find(t)>-1:
                    flag = False
                    break
            if flag:
                count+=1
        return count
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        finds = []
        for word in words:
            flag = True
            for w in word.lower():
                if row1.find(w)<0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                finds.append(word)
                continue
                
            for w in word.lower():
                if row2.find(w)<0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                finds.append(word)
                continue
                
            for w in word.lower():
                if row3.find(w)<0:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                finds.append(word)
        return finds
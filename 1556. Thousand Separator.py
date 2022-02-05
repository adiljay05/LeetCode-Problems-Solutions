class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1].strip()
        string = ""
        count = 0
        for i in range(len(n)):
            string+=n[i]
            count+=1
            if len(n)==i+1:
                break
            if count%3==0:
                string+='.'
            
        return string[::-1]
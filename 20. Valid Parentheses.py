class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []
        counter = 0
        for c in s:
            if c == '(' or c == '{' or c == '[':
                s1.append(c)
                counter+=1
            if c == ')':
                if len(s1)==0:
                    return False
                tmp = s1.pop()
                if tmp == '(':
                    counter-=1
                else:
                    s1.append(tmp)
                    counter+=1
            if c == '}':
                if len(s1)==0:
                    return False
                tmp = s1.pop()
                if tmp == '{':
                    counter-=1
                else:
                    s1.append(tmp)
                    counter+=1
            if c == ']':
                if len(s1)==0:
                    return False
                tmp = s1.pop()
                if tmp == '[':
                    counter-=1
                else:
                    s1.append(tmp)
                    counter+=1
        if counter>0:
            return False
        return True
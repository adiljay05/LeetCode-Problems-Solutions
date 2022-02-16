class Solution:
    def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
        d=dict()
        l=list()
        for i in n1:
            d[i]=d.get(i,0)+1
        for i in n2:
            if d.get(i,0):
                d[i]-=1
                l.append(i)
        return l
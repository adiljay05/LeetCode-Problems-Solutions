class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        strings = [str(integer) for integer in digits]
        a_string = "".join(strings)
        number = int(a_string)
        number+=1
        d = []
        for s in str(number):
            d.append(int(s))
        return d
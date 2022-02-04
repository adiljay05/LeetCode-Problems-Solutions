class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_ = 0
        for s in sentences:
            if len(s.split(' '))>max_:
                max_= len(s.split(' '))
        return max_
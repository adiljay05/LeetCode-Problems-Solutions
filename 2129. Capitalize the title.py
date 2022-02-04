class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title = title.lower().split(' ')
        string = ""
        for t in title:
            if len(t)>2:
                string+= t.capitalize()+" "
            else:
                string += (t+" ")
        return string.strip()
        
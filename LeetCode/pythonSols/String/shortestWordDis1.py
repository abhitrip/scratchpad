class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i,j=-1,-1
        sd = 1<<31
        for idx,word in enumerate(words):
            if word==word1:
                i=idx
            if word==word2:
                j = idx

            if i!=-1 and j!=-1:
                sd = min(sd,abs(i-j))

        return sd

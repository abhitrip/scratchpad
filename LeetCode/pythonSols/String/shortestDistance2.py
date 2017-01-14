class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.wordIdx = collections.defaultdict(list)
        for idx,word in enumerate(words):
            self.wordIdx[word].append(idx)


    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        iword1 = self.wordIdx[word1]
        iword2 = self.wordIdx[word2]
        if not iword1 or not iword2:
            return -1

        i,j=0,0
        sd,word1Idx,word2Idx = (1<<31),-1,-1
        while i<len(iword1) and j<len(iword2):
            word1Idx = iword1[i]
            word2Idx = iword2[j]
            sd = min(sd,abs(word1Idx-word2Idx))
            if word1Idx>word2Idx:
                j+=1
            else:
                i+=1

        return sd




# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")

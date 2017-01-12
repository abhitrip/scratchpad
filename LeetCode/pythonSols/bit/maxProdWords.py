class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bitMap = [0]*len(words)
        for i,word in enumerate(words):
            bitHash = 0
            for ch in word:
                bitHash |= (1<<(ord(ch)-ord('a')))
            bitMap[i] = bitHash
        
        maxProd = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if not bitMap[i]&bitMap[j]:
                    maxProd = max(maxProd,len(words[i])*len(words[j]))
        
        return maxProd
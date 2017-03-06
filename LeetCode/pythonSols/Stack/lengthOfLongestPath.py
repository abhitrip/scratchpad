class Solution(object):
    def lengthLongestPath(self,input):
        """
        :type input: str
        :rtype: int
        """
        stk = []
        maxLen = 0
        allPaths = input.split("\n")
        basePathLen = {0:0}
        currLen = 0
        for path in allPaths:
            level = 0
            while path[level]=='\t': level+=1
            currLen = len(path)-level
            if '.' in path:
                maxLen =  max(maxLen,len(path)-level+basePathLen[level])
            else:
                basePathLen[level+1] = len(path)-level+basePathLen[level]+1
        return maxLen

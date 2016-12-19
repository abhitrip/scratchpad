class Solution(object):

    def findNumOfTabs(self,path):
        cnt  = 0
        while path[cnt]=='\t':
            cnt+=1
        return cnt

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """

        mapOfPaths = collections.defaultdict()
        maxLen = 0


        if '\n' not in input and '.' not in input:
            return 0
        list_of_strs = input.split('\n')



        for string in list_of_strs:
            #print string
            numTabs = self.findNumOfTabs(string)
            if(numTabs>0):
                absfile = mapOfPaths[numTabs-1]+string.replace('\t','')
                if '.' not in absfile:
                    mapOfPaths[numTabs] = absfile+"/"
                #maxLen = max(len(absfile),maxLen)
            elif(numTabs==0):

                absfile = string.replace('\t','')
                if '.' not in absfile:
                    mapOfPaths[numTabs] = absfile+'/'

            if '.' in absfile:
                maxLen = max(len(absfile),maxLen)
            print absfile


        return maxLen


class KMP(object):
    """docstring for KMP"""

    def kmpMatch(self,s,p):
        prefix = self.patternVec(p)
        i,j=0,0
        while i<len(s):
            if s[i]==p[j]:
                i+=1
                j+=1
            else:
                if j!=0:
                    j = prefix[j-1]
                else:
                    i+=1
        if j==len(p): return True
        return False


    def patternVec(self,s):
        prefix = [0]*len(s)

        i,j=1,0
        while i<len(s):
            if s[i]==s[j]:
                prefix[i]=j+1
                j+=1
                i+=1
            else:

                if j!=0:
                    j = prefix[j-1]
                else:
                    i+=1


        return prefix




if __name__=="__main__":
    s = "abxabcabcaby"
    p = "abcaby"
    sol = KMP()
    res = sol.kmpMatch(s,p)
    print res

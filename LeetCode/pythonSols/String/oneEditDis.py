class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sLen,tLen = len(s),len(t)
        if abs(sLen-tLen)>1: return False
        small,big = (s,t) if sLen<tLen else (t,s)
        sLen,bLen = (sLen,tLen) if sLen<tLen else (tLen,sLen)
        
        i,j=0,0
        edits = 0
        while i<sLen and j<bLen:
            if small[i]==big[j]:
                i+=1
                j+=1
            else:
                edits+=1
                if sLen==bLen:
                    i+=1
                    j+=1
                else:
                    j+=1
        
        if edits>1: return False
    
        if edits==1 and 0<=abs(sLen-bLen)<2:
            return True
        
        elif edits==0 and sLen==bLen:
            return False
        
        elif edits==0 and abs(sLen-bLen)==1:
            return True
        
        else:
            return False
            
            
        
        
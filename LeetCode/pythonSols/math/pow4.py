class Solution(object):
    def isPowerOfFour(self,num):
        """
        : type num: int
        : rtype : bool
        """
        cnt = 0
        for i in range(32):
            if (1<<i)&num!=0:
                cnt+=1
                if i%2!=0:
                    return False
        if cnt==1: return True 
        return False

                

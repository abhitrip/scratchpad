class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Bruteforce Matching
        """
        rev = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(rev[i:]):
                return rev[:i]+s
        """
        # KMP matching
        cmbStr=s+'#'+s[::-1]
        print cmbStr
        pat = [0]*len(cmbStr)
        i=1
        j=0
        while i<len(cmbStr):
            if cmbStr[i]==cmbStr[j]:
                pat[i] = j+1
                i+=1
                j+=1
            else:
                if j!=0:
                    j = pat[j-1]
                else:
                    i+=1

        print pat[-1]

        return s[pat[-1]:][::-1]+s








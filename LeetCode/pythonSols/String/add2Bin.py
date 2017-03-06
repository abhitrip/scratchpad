class AddBinary(object):
    """
    Class to add 2 binary integers
    """
    def __init__(self):
        pass
    def addBinary(self,a,b):
        """
        type a : str 
        type b : str
        :rtype : str
        """
        aLen,bLen = len(a),len(b)
        small,big = (a,b) if len(a)<len(b) else (b,a)
        maxLen = max(len(a),len(b))
        i,c=1,0
        res = ""
        while i<maxLen:
            dig1 = int(small[-i] if i<=aLen else "0")
            dig2 = int(big[-i]) 
            s = c +dig1+dig2
            c = s/10
            s = s%10
            res = str(s)+res
            i+=1
        if c==1:
            res = "1"+res
        
        return res


if __name__ == "__main__":
    add = AddBinary()
    print add.addBinary("1","11")

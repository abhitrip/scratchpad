class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        lenList = len(A)
        solExist = False
        idxRev = -1

        if lenList<2:
            return A

        def comp(x,y):
            dig1 = int(str(x)+str(y))
            dig2 = int(str(y)+str(x))
            return dig1-dig2

        i = lenList-1

        if A[i]>A[i-1]:
            A[i-1],A[i] = A[i],A[i-1]
            return A

        while A[i]<A[i-1]:
            i-=1
            if i==1:
                break

        print " i = %d"%i
        if i>1:
            if A[i-1]<A[lenList-1]:
                A[i-1],A[lenList-1]=A[lenList-1],A[i-1]
            b = A[i:]
            revb = A[::-1]
            x = 0
            for k in range(i,lenList):
                A[k] = revb[x]
                x+=1
            return A
        else:
            return sorted(A)

if __name__=="__main__":
    sol = Solution()
    """
    x = [ 251, 844, 767, 778, 658, 337, 10, 252, 632, 262, 707, 506, 701, 475, 410, 696, 631, 903, 516, 149, 344, 101, 42, 891, 991 ]
    """
    x = [1, 2, 3, 6, 5, 4 ]
    '''
    x = [626, 436, 819, 100, 382, 173, 817, 581, 220, 95, 814, 660, 397, 852, 15, 532, 564, 715, 179, 872, 236, 790, 223, 379, 83, 924, 454, 846, 742, 730, 689, 112, 110, 516, 85, 149, 228, 202, 988, 212, 69, 602, 887, 445, 327, 527, 347, 906, 54, 460, 517, 376, 395, 494, 827, 448, 919, 799, 133, 879, 709, 184, 812, 514, 976, 700, 156, 568, 453, 267, 547, 8, 951 ,326, 652, 772, 213, 714, 706, 972, 318, 768, 506, 59, 854, 422]
    '''

    y= sol.nextPermutation(x)
    print y

def countSubstrings(s):
    if not s:
        return 0
    l = len(s)
    count = 0
    i,j,k=0,0,0
    zeros,ones=0,0
    while i<l:
        j = i
        zeros = 0
        while j<l and s[j] ==s[i]:
            j+=1
            zeros+= 1
        count+= min(zeros,ones)
        k = j
        ones = 0
        while k<l and s[k]==s[j]:
            k+=1
            ones+=1
        count+= min(zeros,ones)
        i = k
    return count

def countSubs(s):
    if not s:
        return 0
if __name__=="__main__":
    s = "00101"
    print countSubstrings(s)
00

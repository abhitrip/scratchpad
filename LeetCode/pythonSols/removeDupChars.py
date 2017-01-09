class Solution(object):
    def removeDuplicateLetters2(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        while s:
            minIdx = min(map(s.rindex,set(s)))
            minChar = min(s[:minIdx+1])
            firstIdx = s.index(minChar)
            s = s[firstIdx:].replace(minChar,'')
            result.append(minChar)
        return ''.join(result)


    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        idxMap = {c:i for i,c in enumerate(s)}
        size,i = len(idxMap),0
        beg,end = 0,0
        while i<size:
            end = reduce(min,idxMap.values())

            minChar = chr(ord('z')+1)
            start = beg
            while start<=end:
                if (s[start] in idxMap) and minChar>s[start]:
                    minChar = s[start]
                    beg = start+1
                start+=1

            result+= minChar
            del idxMap[minChar]
            i+=1

        return result




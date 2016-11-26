class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        """
        The logic is to keep the added value at the start index
        Also Keep the negative of added value at end index +1
        So, it's like :
        0,2,0,0,-2 #1,3,2
        0,2,3,0,-2  #2,4,3
        -2,2,3,2,-2,  #0,2,-2
        Now,sum all elemnts till that point to get res
        -2,0,3,5,3
        """
        modified = [0 for i in range(length)]
        for start,end,update in updates:
            modified[start] += update
            if end+1<len(modified):
                modified[end+1] -= update

        print modified
        cumSum = 0
        for idx,val in enumerate(modified):
            cumSum+=val

            modified[idx] = cumSum


        return modified

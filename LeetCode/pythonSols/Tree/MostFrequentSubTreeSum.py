# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.left = None

#         self.right = None



class Solution(object):

    def findFrequentTreeSum(self, root):

        """

        :type root: TreeNode

        :rtype: List[int]

        """

        mapSum = collections.Counter()

        maxCnt=[0]

        def postorder(root,maxCnt):

            if not root: return 0

            currSum = postorder(root.left,maxCnt)

            currSum +=postorder(root.right,maxCnt)

            currSum += root.val

            mapSum[currSum]+=1

            maxCnt[0] = max(maxCnt[0],mapSum[currSum])

            return currSum

        

        postorder(root,maxCnt)

        #print mapSum

        res = [key for key in mapSum if mapSum[key]==maxCnt[0]]

        return res

        

        

            

        

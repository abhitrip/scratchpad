class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        maxLen,left = 0,-1
        for idx,ch in enumerate(s):
            if s[idx]=='(':
                stack.append(idx)
            else:
                if not stack:
                    left = idx
                else:
                    stack.pop()
                    maxLen = max(maxLen, idx-left  if not stack else idx-stack[-1])

        return maxLen


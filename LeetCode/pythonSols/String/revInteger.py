class Solution(object):

    def reverse(self, x):

        """

        :type x: int

        :rtype: int

        """

        strx = str(abs(x))

        rev = int(strx[::-1] if x>=0 else '-'+strx[::-1])

        return rev if -(1<<31)<rev<(1<<31) else 0

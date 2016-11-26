class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """


        people.sort(key= lambda x:(-x[0],x[1])) # Sorting List by decreasing height and increasing num of people in front of it
        res = []
        for person in people:
            idx = person[1]
            res.insert(idx,person)

        return res

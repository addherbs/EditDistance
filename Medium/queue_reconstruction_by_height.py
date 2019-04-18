class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort (key=lambda x: x[1])
        people.sort (key=lambda x: x[0], reverse=True)
        result = []

        for p in people:
            result.insert (p[1], p)

        return result
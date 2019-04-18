class Solution (object):
    def __init__(self):
        self.visited = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort ()
        self._check (nums, [])

        return list (self.visited)

    def _check(self, ip, output):

        print ("ip {} op {}".format (ip, output))
        if (not ip):
            if (output not in self.visited):
                self.visited.append (output)
        else:
            self._check (ip[1:], output)
            self._check (ip[1:], output + [ip[0]])


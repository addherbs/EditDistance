# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start = sorted ([x.start for x in intervals])
        end = sorted ([x.end for x in intervals])

        room = end_index = 0
        print (start, end)
        for start_index in range (len (start)):
            if (start[start_index] < end[end_index]):
                room += 1
            else:
                end_index += 1

        return room
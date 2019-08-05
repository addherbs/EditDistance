# 539. Minimum Time Difference
# Medium
#
# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
# Example 1:
# Input: ["23:59","00:00"]
# Output: 1
# Note:
# The number of time points in the given list is at least 2 and won't exceed 20000.
# The input time is legal and ranges from 00:00 to 23:59.


class Solution:
    def findMinDifference(self, timePoints):
        minutes = []
        for each_time in timePoints:
            minutes.append(self.cal_mins(each_time))
        minutes.sort()
        min_diff = max(minutes)
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        print(minutes)
        min_diff = min(min_diff, 1440 - minutes[-1] + minutes[0])
        return min_diff

    def cal_mins(self, time):
        hour, mins = time.split(":")
        return int(hour) * 60 + int(mins)


sol = Solution()
tests = [[["23:59", "00:00"], 1], [["05:31", "22:08", "00:35"], 147]]

for test in tests:
    ans = test[1]
    value = sol.findMinDifference(test[0])
    print("ans: ", ans == value, ans, value)

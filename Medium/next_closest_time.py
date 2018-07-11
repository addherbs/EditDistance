class Solution:
    def nextClosestTime(self, time):

        ih, im = int (time.split (":")[0]), int (time.split (":")[1])
        current_mins = ih * 60 + im

        digits = set (x for x in time if (x.isdigit ()))
        hours, mins = self.gen (digits)

        all_times_list = sorted ([h * 60 + m for h in hours for m in mins])

        fh, fm = divmod (all_times_list[(all_times_list.index (current_mins) + 1) % len (all_times_list)], 60)

        return "{:02d}:{:02d}".format (fh, fm)

    def gen(self, digits):
        hours = []
        mins = []
        for i in digits:
            for j in digits:
                cur = int (i + j)
                if (cur < 60): mins.append (cur)
                if (cur < 24): hours.append (cur)

        return hours, mins
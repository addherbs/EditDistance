class MaxStack (object):
    def __init__(self):
        import sys
        self.max = [- sys.maxsize, -1]
        self.stack = []

    def push(self, x):

        if (not self.stack):
            self.max[0] = x
            self.max[1] = 0

        elif (x >= self.max[0]):
            self.max[0] = x
            self.max[1] = len (self.stack)

        self.stack.append (x)

    def pop(self):

        if (len (self.stack) == 0):
            return None
        else:
            if (len (self.stack) == 1):
                self.max[0] = - sys.maxsize
                self.max[1] = -1
            elif (self.max[0] == self.stack[-1] and self.max[1] == len (self.stack) - 1):

                next_max = - sys.maxsize
                index = -1
                for i in range (0, len (self.stack) - 1):
                    if (self.stack[i] >= next_max):
                        index = i
                        next_max = self.stack[i]

                self.max[0] = next_max
                self.max[1] = index

            return self.stack.pop ()

    def top(self):

        if (not self.stack):
            return None
        else:
            return self.stack[-1]

    def peekMax(self):

        return self.max[0]

    def popMax(self):
        """
        :rtype: int
        """
        if (not self.stack): return None
        return_val = self.max[0]

        self.stack.pop (self.max[1])

        next_max = - sys.maxsize
        index = -1
        for i in range (0, len (self.stack)):
            if (self.stack[i] >= next_max):
                index = i
                next_max = self.stack[i]

        self.max[0] = next_max
        self.max[1] = index

        return return_val




        # Your MaxStack object will be instantiated and called as such:
        # obj = MaxStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.peekMax()
        # param_5 = obj.popMax()
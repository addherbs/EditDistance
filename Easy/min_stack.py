class MinStack (object):
    def __init__(self):
        import sys
        self.min = [sys.maxsize, -1]
        self.stack = []

    def push(self, x):

        if (not self.stack):
            self.min[0] = x
            self.min[1] = 0

        elif (x < self.min[0]):
            self.min[0] = x
            self.min[1] = len (self.stack)

        self.stack.append (x)

    def pop(self):

        if (len (self.stack) == 0):
            return None
        else:
            if (len (self.stack) == 1):
                self.min[0] = sys.maxsize
                self.min[1] = -1
            elif (self.min[0] == self.stack[-1] and self.min[1] == len (self.stack) - 1):

                next_min = sys.maxsize
                index = -1
                for i in range (0, len (self.stack) - 1):
                    if (self.stack[i] < next_min):
                        index = i
                        next_min = self.stack[i]

                self.min[0] = next_min
                self.min[1] = index

            self.stack.pop ()
            return None

    def top(self):
        """
        :rtype: int
        """
        if (not self.stack):
            return None
        else:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[0]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
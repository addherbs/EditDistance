class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.list = []
        self.len = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """

        if (self.get_len () == self.size): self.list.pop (0)

        self.list.append (val)
        self.set_len ()
        return sum (self.list) / self.get_len ()

    def set_len(self):
        self.len = len (self.list)

    def get_len(self):
        return self.len

        # Your MovingAverage object will be instantiated and called as such:
        # obj = MovingAverage(size)
        # param_1 = obj.next(val)
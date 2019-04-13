class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = list (nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        if (len (self.nums) == 1):
            return self.nums

        output = list (self.nums)
        for x in range (len (output) - 1):
            place1 = random.randint (x, len (output) - 1)
            output[place1], output[x] = output[x], output[place1]

            # random.shuffle(output)
        return output


        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.reset()
        # param_2 = obj.shuffle()
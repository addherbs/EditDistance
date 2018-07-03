class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for each in matrix:
            print ("each: ", each)
            if (not each):
                return False
            if (target >= each[0] and target <= each[-1]):
                if (self.bin_search (each, target)):
                    return True
        return False

    def bin_search(self, lis, target):
        l = 0
        h = len (lis)
        m = (l + h) // 2

        while (l <= h):
            m = (l + h) // 2
            if (lis[m] == target):
                return True
            else:
                if (lis[m] < target):
                    l = m + 1
                else:
                    h = m - 1
        return False

x = Solution()
m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5

print(x.searchMatrix(m,target))
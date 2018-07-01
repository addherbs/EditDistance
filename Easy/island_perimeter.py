class Solution (object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        row = len (grid)
        col = len (grid[0])

        check = lambda x, y: 0 if (x < 0 or x >= row or y < 0 or y >= col) else grid[x][y]
        final = 0
        for i in range (0, row):
            for j in range (0, col):
                if (grid[i][j] == 1):
                    val = 4 - (check (i + 1, j) + check (i - 1, j) + check (i, j + 1) + check (i, j - 1))
                    final += val

        print (final)
        return final
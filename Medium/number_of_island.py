class Solution (object):
    def __init__(self):
        self.visited = self.grid = None
        self.count = 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if (not grid):
            return 0

        r = len (grid);
        c = len (grid[0])
        self.visited = [[0] * c for _ in range (r)]
        self.grid = grid

        for i in range (r):
            for j in range (c):
                if (self.visited[i][j] != 1 and grid[i][j] == "1"):
                    self.count += 1
                    self._call (i, j)

        return self.count

    def _call(self, i, j):
        if (i < 0 or i >= len (self.visited) or j < 0 or j >= len (self.visited[0])):
            return None
        elif (self.visited[i][j] == 1 or self.grid[i][j] == "0"):
            return None
        else:
            self.visited[i][j] = 1
            self._call (i, j - 1)
            self._call (i - 1, j)
            self._call (i + 1, j)
            self._call (i, j + 1)
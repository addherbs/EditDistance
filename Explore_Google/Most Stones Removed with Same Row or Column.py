"""
Most Stones Removed with Same Row or Column

Solution
On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0
 

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""


# Solution using DFS, Time Complexity O(N ** 2)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        to_visit = {(r, c) for r, c in stones}
        
        rows_adj_list = defaultdict(list)
        cols_adj_list = defaultdict(list)
        for x, y in stones: 
            rows_adj_list[x].append(y)
            cols_adj_list[y].append(x)

        count = 0
        
        # Call for DFS
        for x, y in stones:
            if (x, y) in to_visit:
                count += 1
                
                # print(x, y)
                
                stack = [(x, y)]
                
                while stack:
                    x, y = stack.pop()
                    if (x, y) not in to_visit: continue
                    to_visit.remove((x, y))
                    for col_index in rows_adj_list[x]:
                        stack.append((x, col_index))
                    
                    for row_index in cols_adj_list[y]:
                        stack.append((row_index, y))
        
        return len(stones) - count
        
        
        
# Using Disjoin Set method. Time complexity is O(N * LOG(N))
class DisjoinSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    
    def find_path_compression(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_path_compression(self.parent[x])
        
        return self.parent[x]
    
    
    def union(self, x, y):
        
        # With union-by-rank method, optimization
        x_set_rep = self.find_path_compression(x)
        y_set_rep = self.find_path_compression(y)
        
        if x_set_rep == y_set_rep: return
        
        if self.rank[x_set_rep] > self.rank[y_set_rep]:
            self.parent[y_set_rep] = x_set_rep
        elif self.rank[x_set_rep] < self.rank[y_set_rep]:
            self.parent[x_set_rep] = y_set_rep
        else:
            self.parent[x_set_rep] = y_set_rep
            self.rank[y_set_rep] += 1
        
        # Without Union-by-rank method
        # xr = self.find_path_compression(x)
        # yr = self.find_path_compression(y)
        # self.parent[xr] = yr
    

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        dsu = DisjoinSet(20001)
        
        for x, y in stones:
            dsu.union(x, y + 10000)
        
        return len(stones) - len({dsu.find_path_compression(x) for x, y in stones})
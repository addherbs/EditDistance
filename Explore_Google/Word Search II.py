"""
212. Word Search II
Hard

3140

130

Add to List

Share
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie =  self.create_trie(words)
        m, n = len(board), len(board[0])
        result = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    self.backtrack(trie[board[i][j]], board, i, j, result)
                    if not trie[board[i][j]]:
                        trie.pop(board[i][j])

        return result

    
    def backtrack(self, trie, grid, i, j, result):
        from pprint import pprint as pp
        
        if "#" in trie:
            result.append(trie["#"])
            trie.pop("#")

        val, grid[i][j]  = grid[i][j], "end"

        for each in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x, y = i + each[0], j + each[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != "end" and grid[x][y] in trie:
                self.backtrack(trie[grid[x][y]], grid, x, y, result)
                #### Optimization Lines ###
                if not trie[grid[x][y]]:
                    trie.pop(grid[x][y])
                #### Optimization Lines ###


        grid[i][j] = val


    def create_trie(self, words):

        END_WORD = "#"
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                if ch in node:
                    node = node[ch]
                else:
                    node[ch] = {}
                    node = node[ch]
            else:
                node[END_WORD] = word

        return trie
        
        


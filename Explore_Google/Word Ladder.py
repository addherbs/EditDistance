"""
Word Ladder

Solution
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""



class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not beginWord or not endWord or endWord not in wordList: return 0
        
        self.L = len(beginWord)
        self.combos = defaultdict(list)
        
        # Generating all the combinations of a word
        for word in wordList:
            for i in range(self.L):
                self.combos[word[:i] + "#" + word[i+1:]].append(word)
        
        
        v1, v2 = {beginWord: 1}, {endWord: 1}
        queue1, queue2 = collections.deque(), collections.deque()
        queue1.append((beginWord, 1))
        queue2.append((endWord, 1))
        
        while queue1 and queue2:
            
            ans = self.BFS(queue1, v1, v2)
            if ans:
                return ans
            
            ans = self.BFS(queue2, v2, v1)
            if ans:
                return ans
            
        return 0
    
    
    def BFS(self, queue, v1, v2):
        
        wd, level = queue.popleft()
        
        for i in range(self.L):
            intermediate_word = wd[:i] + "#" + wd[i+1:]
            for word in self.combos[intermediate_word]:
                if word in v2:
                    return v2[word] + level
                if word not in v1:
                    v1[word] = level + 1
                    queue.append((word, level+1))
        
        return None
    
    
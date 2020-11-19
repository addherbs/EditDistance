"""
Expressive Words

Solution
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has size less than 3.  Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Constraints:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""
class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        ans = 0

        S_count = self.ch_counter(S)

        for each in words:
            each_count = self.ch_counter(each)
            if len(S_count) != len(each_count) or len(S) < len(each):   continue
            for i in range(len(each_count)):
                if each_count[i][0] != S_count[i][0]:   break
                if int(S_count[i][1:]) < 3 and (int(S_count[i][1:]) != int(each_count[i][1:])): break
                if int(S_count[i][1:]) < int(each_count[i][1:]): break
            else:
                ans += 1
        return ans
            
    def ch_counter(self, word):
        
        cnt = 1
        ans = []
        for i in range(len(word)):
            if i + 1 < len(word):
                if word[i + 1] == word[i]:
                    cnt += 1
                else:
                    ans.append(word[i] + str(cnt))
                    cnt = 1
            else:
                ans.append(word[i] + str(cnt))

        return ans

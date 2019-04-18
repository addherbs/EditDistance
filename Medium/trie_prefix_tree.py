class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.child = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode ()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        node = self.root
        for each in word:
            if (each not in node.child):
                node.child[each] = TrieNode ()
            node = node.child[each]

        node.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for each in word:
            if (each not in node.child):
                return False
            node = node.child[each]

        return node.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for each in prefix:
            if each not in node.child:
                return False
            node = node.child[each]

        return True

        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)
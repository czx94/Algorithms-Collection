class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        tree = self.tree
        for w in word:
            if w in tree:
                tree = tree[w]
            else:
                tree[w] = {}
                tree = tree[w]

        tree[0] = [0]

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tree = self.tree
        while word:
            try:
                tree = tree[word[0]]
                word = word[1:]
            except:
                return False

        return True if tree.has_key(0) else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tree = self.tree
        while prefix:
            try:
                tree = tree[prefix[0]]
                prefix = prefix[1:]
            except:
                return False

        return True


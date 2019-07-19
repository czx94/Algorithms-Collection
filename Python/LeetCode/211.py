import collections

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words_dict = collections.defaultdict(list)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if word:
            self.words_dict[len(word)].append(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False

        if '.' not in word:
            return word in self.words_dict[len(word)]
        else:
            for match in self.words_dict[len(word)]:
                for index, c in enumerate(word):
                    if c != '.' and c != match[index]:
                        break
                else:
                    return True

            return False
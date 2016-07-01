# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# For example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true


class WordDictionary1(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.len2words = collections.defaultdict(list)


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.len2words[len(word)].append(word)        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        words = self.len2words[len(word)]
        for i, char in enumerate(word):
            words = [w for w in words if char in (".", w[i])]
            if not words: return False
        return True

        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

class WordDictionary12(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False

        if '.' not in word:
            return word in self.word_dict[len(word)]

        for v in self.word_dict[len(word)]:
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False







# Python easy to follow solution using Trie.

class TrieNode():
    def __init__(self):
        self.childs = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.childs[w]
        node.isWord = True

    def search(self, word):
        node  = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return

        if word[0] == '.':
            for n in node.childs.values():
                self.dfs(n, word[1:])
        else:
            node = node.childs.get(word[0])
            if not node:
                return
            self.dfs(node, word[1:])
































































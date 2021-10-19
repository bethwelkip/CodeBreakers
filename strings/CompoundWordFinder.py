# please run using python3


import sys

# trie nodes


class Node:
    def __init__(self, word="", isWord=False):
        self.neigh = {}
        self.isWord = isWord
        self.word = word

    def __str__(self):
        return str(self.neigh)


class CompoundWordFinder:
    # initialize trie and a list to store compound words
    def __init__(self):
        self.trie = Node()
        self.res = []

    # search if word is a compound word
    def search(self, start, word):
        root = self.trie
        i = start
        while i < len(word):
            if root.isWord:
                return (True, root.word, i)
            if word[i] in root.neigh:
                root = root.neigh[word[i]]
            else:
                return (False, '', float('inf'))
            i += 1
        return (True, root.word, i)

    # insert word in trie while checking if compound
    def insert(self, word):
        root = self.trie
        end_index = 0
        seen_words = set()
        for i in range(len(word)):
            if end_index == i:
                (isWord, com_word, index) = self.search(i, word)
                end_index = index
                if isWord:
                    if com_word not in seen_words and len(com_word) > 0:
                        seen_words.add(com_word)
                    else:
                        end_index = float('inf')

            if word[i] in root.neigh:
                root = root.neigh[word[i]]
            else:
                root.neigh[word[i]] = Node()
                root = root.neigh[word[i]]

        root.isWord = True
        root.word = word
        # if a compound word, add to list of compound words
        if end_index == len(word) and len(seen_words) > 1:
            self.res.append(word)


if __name__ == '__main__':
    raw_words = []  # ["man", "dragon", "manwomanflyrace", "woman", "manhandlebag", "bag","handle", "fly", "race", "dragonfly", "car", "racecar", "flydragon", "manbag"]

    sample = CompoundWordFinder()
    for line in sys.stdin:
        raw_words.append(line.strip())

    words = sorted(raw_words, key=lambda word: len(word))
    for word in words:
        sample.insert(word)

    # write out the compound words
    compound_words = sorted(sample.res)
    for i in range(len(sample.res)):
        sys.stdout.write(compound_words[i]+'\n')

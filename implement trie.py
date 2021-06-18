class TrieNode:
    def __init__(self):
        self.end = False
        self.keys = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, node=None):
        if node is None:
            node = self.root

        if len(word) == 0:
            node.end = True
            return

        if word[0] not in node.keys:
            node.keys[word[0]] = TrieNode()
            self.insert(word[1:], node.keys[word[0]])

        else:
            self.insert(word[1:], node.keys[word[0]])

    def search(self, word, node=None):
        if node is None:
            node = self.root

        if len(word) == 0 and node.end == True:
            return True

        if len(word) == 0 and node.end == False:
            return False

        if word[0] not in node.keys:
            return False

        return self.search(word[1:], node.keys[word[0]])

    def starts_with(self, prefix, node=None):
        if node is None:
            node = self.root

        if len(prefix) == 0:
            return True

        if prefix[0] not in node.keys:
            return False

        return self.starts_with(prefix[1:], node.keys[prefix[0]])


t = Trie()

t.insert('apple')
t.insert('dog')

print(t.search('apple'))
print(t.search('app'))

t.insert('app')
print(t.search('app'))

print(t.starts_with('do'))

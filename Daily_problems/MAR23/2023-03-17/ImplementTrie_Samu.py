class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie['_'] = {}

    def search(self, word: str) -> bool:
        trie = self.trie
        for char in word:
            if char not in trie:
                return False
            trie = trie[char]
        if '_' in trie:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for char in prefix:
            if char not in trie:
                return False
            trie = trie[char]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
obj.search('app')
obj.startsWith('app')
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
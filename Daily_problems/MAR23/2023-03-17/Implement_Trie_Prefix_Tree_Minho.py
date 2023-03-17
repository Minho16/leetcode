class Trie:
    def __init__(self):
        self.word_dict = {}

    def insert(self, word: str) -> None:
        first_letter = word[0]
        if first_letter in self.word_dict.keys():
            self.word_dict[first_letter].append(word)
        else:
            self.word_dict[first_letter] = [word]

    def search(self, word: str) -> bool:
        if word[0] in self.word_dict.keys():
            if word in self.word_dict[word[0]]:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        len_prefix = len(prefix)
        found = False
        if prefix[0] in self.word_dict.keys():
            for word in self.word_dict[prefix[0]]:
                if word[:len_prefix] == prefix:
                    found = True
                    break
        return found

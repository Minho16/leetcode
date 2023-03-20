# 211. Design Add and Search Words Data Structure
class WordDictionary:

    def __init__(self):
        self.Dictionary = {}

    def addWord(self, word: str) -> None:
        d = self.Dictionary
        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]
        d['.'] = {} 


    def search(self, word: str) -> bool:
        candidates = [self.Dictionary]
        for char in word:
            c2 = []
            if char == '.':
                for dict in candidates:
                    c2.append(list(dict.values))
            else:
                for dict in candidates:
                    if char in dict:
                        c2.append(dict[char])
            candidates = c2
            if len(candidates) == 0:
                return False
        for dict in candidates:
            if '.' in dict:
                return True
        return False
# Approach using Lists (14 Test passed, TLE)
class WordDictionary2:

    def __init__(self):
        self.Dictionary = []

    def addWord(self, word: str) -> None:
        if word not in self.Dictionary:
            self.Dictionary.append(word)

    def search(self, word: str) -> bool:
        candidates = []
        for d in self.Dictionary:
            if len(d) == len(word):
                candidates.append(d)
        for i, c in enumerate(candidates):
            result = True
            for j, char in enumerate(word):
                if char != '.' and c[j] != char:
                    result = False
            if result:
                return True
        return False


a = WordDictionary()
a.addWord('at')
a.addWord('and')
a.addWord('an') 
a.addWord('add') 
a.search('a') # False
a.search('.at') # False
a.addWord('bat') 
a.search('.at') # True
a.search('an.') # True
a.search('a.d.') # False
a.search('b.') # False
a.search('a.d') # True
a.search('.') # False
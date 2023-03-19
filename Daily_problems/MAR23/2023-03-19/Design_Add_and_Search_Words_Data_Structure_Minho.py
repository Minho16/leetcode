class WordDictionary:
    def __init__(self):
        self.words_dictionary = {}

    def addWord(self, word: str) -> None:
        first_letter = word[0]
        if first_letter in self.words_dictionary:
            self.words_dictionary[first_letter].append(word)
        else:
            self.words_dictionary[first_letter] = [word]

    def search(self, word: str) -> bool:
        def check_if_word_with_dot_in_list(word, checking_word) -> bool:
            found = False
            # check if the length is the same
            if len(word) == len(checking_word):
                for idx, letter in enumerate(word):
                    if letter == '.':
                        checking_word = checking_word[:idx] + '.' + \
                            checking_word[idx+1:]
                if word == checking_word:
                    found = True
            return found

        if '.' in word:
            if '.' == word[0]:
                found = False
                for _, list_values in self.words_dictionary.items():
                    if found:
                        break
                    for value in list_values:
                        if found:
                            break
                        found = check_if_word_with_dot_in_list(word, value)
                return found

            else:
                if not word[0] in self.words_dictionary.keys():
                    return False

                list_to_check = self.words_dictionary[word[0]]
                for item in list_to_check:
                    found = check_if_word_with_dot_in_list(word, item)
                    if found:
                        break
                return found
        else:
            if word[0] in self.words_dictionary.keys():
                if word in self.words_dictionary[word[0]]:
                    return True
            else:
                return False
        return False


# Your WordDictionary object will be instantiated
# and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

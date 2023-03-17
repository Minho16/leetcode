class Solution:
    def isAlienSorted(self, words: list, order: str) -> bool:
        if len(words) == 1:
            return True

        else:
            nums = [i for i in range(1, len(order) + 1)]

            order_dict = dict(zip(order, nums))

            # need to compare 2 words consecutively
            for idx, word in enumerate(words):
                if idx != len(words) - 1:
                    for i, char in enumerate(word):
                        if i >= len(words[idx + 1]):
                            return False
                        if order_dict[char] == order_dict[words[idx + 1][i]]:
                            pass
                        elif order_dict[char] > order_dict[words[idx + 1][i]]:
                            return False
                        elif order_dict[char] < order_dict[words[idx + 1][i]]:
                            break
            return True


s = Solution()
words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(s.isAlienSorted(words, order))

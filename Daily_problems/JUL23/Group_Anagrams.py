class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Group by words that share same characters

        1. For each word, sort in ascending order and save this word as possible key
        2. Create a dictionary where key = sorted word and value = list[words]
        3. Return all the values as output

        """
        words_dict: dict = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string in words_dict.keys():
                words_dict[sorted_string].append(string)
            else:
                words_dict[sorted_string] = [string]

        return [value for value in words_dict.values()]

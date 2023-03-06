class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        dict_saving_point = {'found': []}
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                if haystack[i: i + len(needle)] == needle:
                    dict_saving_point['found'].append(i)
                    i += len(needle) - 1 
            i += 1
        
        if dict_saving_point['found'] == []:
            return -1 
        else:
            return dict_saving_point['found'][0]
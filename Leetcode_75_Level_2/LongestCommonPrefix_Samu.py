# 14. Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_s = min(strs, key=len)
        l = len(min_s)-1
        for word in strs:
            l2 = l
            while l2 >= 0:
                if word[l2] != min_s[l2]:
                    min_s = min_s[:l2]
                    l = l2-1 
                l2 -=1
        return min_s
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m,n = len(haystack),len(needle)
        end = m-n+1
        for i in range (end):
            if haystack[i:i+n] == needle:
                return i
        return -1
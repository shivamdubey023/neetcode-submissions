class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for word in s:
            if word.isalnum():
                clean += word.lower()
        rev = ""
        for char in clean:
            rev= char + rev
        return clean == rev

        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        rev= ""
        for word in s: 
            if word.isalnum(): 
                clean += word.lower()
        for char in clean:
            rev = char+ rev
        return rev == clean

        
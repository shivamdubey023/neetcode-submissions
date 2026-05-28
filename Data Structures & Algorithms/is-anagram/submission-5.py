class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test ={}
        test1 ={}
        for char in s:
            if char in test:
                test[char]+=1
            else :
                test[char]=1

        for char in t:
            if char in test1:
                test1[char]+=1
            else :
                test1[char]=1

        return test == test1
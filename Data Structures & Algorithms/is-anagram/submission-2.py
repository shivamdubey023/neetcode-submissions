class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            store1 = {}
            store2 = {}
            for char in s:
                if char in store1:
                    store1[char] += 1
                else:
                    store1[char] = 1

            for char in t:
                if char in store2:
                    store2[char] +=1
                else:
                    store2[char]=1
            return store1 == store2
                    


            

         
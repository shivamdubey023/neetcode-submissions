class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range (n):
            max_right =-1 
            for j in range (i+1,n):
                max_right = max(max_right, arr[j])
            arr[i]=max_right
        # arr.sort(key=abs,reverse= True)
        return arr
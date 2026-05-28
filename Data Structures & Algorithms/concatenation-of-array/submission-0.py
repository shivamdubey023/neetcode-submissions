class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        test=[]
        for num in nums:
            test.append(num)
        final = test+test
        return final
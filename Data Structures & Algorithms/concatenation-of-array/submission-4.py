class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        sum_arr = []
        for num in nums:
            sum_arr.append(num) 
        return nums + sum_arr
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set()

        for num in nums :
            test.add(num)

        return len(nums) != len(test) 
            
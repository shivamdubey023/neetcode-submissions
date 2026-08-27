class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0 
        rightsum = 0 
        for index, value in enumerate(nums):
            rightsum = total - leftsum - value
            if leftsum == rightsum:
                return index
            else:
                leftsum += value
        return -1
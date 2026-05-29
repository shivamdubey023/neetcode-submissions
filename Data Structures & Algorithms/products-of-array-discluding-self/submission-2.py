class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for num in range (len(nums)):
            product = 1
            for j in range (len(nums)):
                if num != j:
                    product *= nums[j]

            result.append(product)

        return result
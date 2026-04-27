class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []


        for i in range(len(nums)):
            prod = 1
            
            # product of right
            for j in range(i + 1, len(nums)):
                if i == j: continue
                prod *= nums[j]

            for j in range(i + 1):
                if i == j:
                    continue
                prod *= nums[j]

            output.append(prod)

        return output

                

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_counter = 0
        for num in nums:
            if num == 0:
                zero_counter+=1
                num = 1
            product = product * num
        output = []
        for num in nums:
            if zero_counter == 0:
                output.append(int(product/num))
            if zero_counter == 1:
                if num == 0:
                    num = 1
                    output.append(int(product/num))
                else:
                    output.append(0)
            elif zero_counter >= 2:
                output.append(0)

        return output
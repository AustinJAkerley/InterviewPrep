class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        i = 0
        for num in nums:
            if num in numMap.keys():
                return [numMap[num], i]
            numMap.update({target-num:i})
            i+=1
        return None
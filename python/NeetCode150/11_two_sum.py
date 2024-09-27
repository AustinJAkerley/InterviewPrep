class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(0, len(numbers)):
            diff = target - numbers[i]
            res = numMap.get(diff)
            if res is not None:
                return [res + 1, i + 1]
            numMap.update({numbers[i]:i})
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        output = []
        for i in range(0, k):
            biggest = (None, 0)
            for key in num_count:
                if num_count[key] > biggest[1]:
                    biggest = (key, num_count[key])
            num_count.pop(biggest[0])
            output.append(biggest[0])
        return output

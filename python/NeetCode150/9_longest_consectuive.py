class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        largest = 0
        for num in numSet:
            if num-1 in numSet:
                continue
            else:
                size = 1
                while num+1 in numSet:
                    size+=1
                    num+=1
                if size > largest:
                    largest = size
        return largest

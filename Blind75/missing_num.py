########################
# name: helixplant
# file: missing number
# date: oct. 10, 2024
#
# difficulty: easy
# time to finish: 4mins
# 
# comments:
#   fairly simple problem, not too much complexity in execution in python
#   can be improved, runtime is not great
# 
########################

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] != i: #given nums is ordered, if not == then return i
                return i
        return i + 1 #if all values are present, then must be next num
        
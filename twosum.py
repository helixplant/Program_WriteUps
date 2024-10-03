########################
# name: helixplant
# file: two sum
# date: oct. 2, 2024
#
# difficulty: easy
# time to finish: <5mins
# 
# comments:
#   extremely easy
#   probably could have done a different search 
#   for lower time complexity
# 
########################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums is int array
        # target is int

        # search
        for i in range(0, len(nums)):
            for j in range((i+1), len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
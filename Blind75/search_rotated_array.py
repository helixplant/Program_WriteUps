########################
# name: helixplant
# file: search in rotated sorted array
# date: oct. 4, 2024
#
# difficulty: medium
# time to finish: 15min
# 
# comments:
#   i overthought this problem initially
#   34ms runtime, beats 96.25% which is wild considering the difficulty
#   i was initially confused by the question but it 
#   was straight forward, surprisingly (again)
#
#   could switch language or half search to reduce run time
# 
########################

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #we have target and array
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
        return -1
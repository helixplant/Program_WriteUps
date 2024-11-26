########################
# name: helixplant
# file: best time to buy and sell stock
# date: oct. 3, 2024
#
# difficulty: medium
# time to finish: <1min
# 
# comments:
#   extremely easy
#   36ms runtime, beats 90.82%
#   i was initially confused by the question but it 
#   was straight forward, surprisingly
#
#   could also go from left to right and when prev num > curr num
#   immediately return curr num
# 
########################

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
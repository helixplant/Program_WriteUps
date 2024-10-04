########################
# name: helixplant
# file: copy of array except self
# date: oct. 3, 2024
#
# difficulty: medium
# time to finish: 15 mins
# 
# comments:
#   would have been easier with multiplication, but might
#   have some weird edge cases with zeros
# 
########################

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(n) time, no divide
        temp = 1
        arr = [1 for _ in range(len(nums))] #populate array with 1 so not None
        for i in range(0, len(nums)): #for loop will always be valid since len is always 2 or more
            arr[i] *= temp
            temp *= nums[i]
        temp = 1 #reset temp, start from top
        for j in range(len(nums)-1, -1, -1): #for loop with decrement
            arr[j] *= temp
            temp *= nums[j]
        return arr
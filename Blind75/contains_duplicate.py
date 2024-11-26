########################
# name: helixplant
# file: contains duplicate
# date: oct. 3, 2024
#
# difficulty: easy
# time to finish: <5mins
# 
# comments:
#   sorting puts like numbers together and lowers the complexity of the question
# 
########################


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #sort for ease
        nums.sort()
        #temp value, set at index 0 initially
        temp = nums[0]
        if len(nums) <= 1: #no duplicates for len <= 1
            return False
        #look through list 
        for i in range(1, len(nums)):
            if temp == nums[i]: #duplicate exists
                return True
            temp = nums[i] #update temp otherwise
        return False

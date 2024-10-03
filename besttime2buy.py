########################
# name: helixplant
# file: best time to buy and sell stock
# date: oct. 3, 2024
#
# difficulty: easy
# time to finish: <8mins
# 
# comments:
#   extremely easy
#   brute force solution would traverse too much and prove inefficient
# 
########################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices is int array
        min = prices[0] #the most minimum value we can achieve, init to first val
        profit = 0 #the largest profit we can receive 
        for i in range(0, len(prices)):
            if prices[i] < min: #if current value is lower than prev min, change
                min = prices[i]
            elif (prices[i] - min) > profit: #see if profit is greater
                profit = prices[i] - min
        return profit

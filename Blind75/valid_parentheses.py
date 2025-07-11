########################
# name: helixplant
# file: valid parentheses
# date: july 11, 2025
#
# difficulty: easy
# time to finish: <8mins
# 
# comments:
#   extremely easy!
#   beats 100.00% in runtime omg
# 
########################

class Solution:
    def isValid(self, s: str) -> bool:
        list = []
        for c in s:
            if c == '(':
                list.append(')')
            elif c == '[':
                list.append(']')
            elif c == '{':
                list.append('}')
            elif len(list)>0 and c == list[len(list)-1]:
                list.pop()
            elif c not in list:
                return False
        if len(list) > 0:
            return False
        return True  
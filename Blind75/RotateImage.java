/*########################
# name: helixplant
# file: rotate image
# date: july 14, 2025
#
# difficulty: medium
# time to finish: >15mins
# 
# comments:
#   it took a while to get the right idea for 
#   rotating, but I figured this was a fool-proof
#   approach, and it has 0ms of runtime!
# 
########################*/

class Solution {
    public void rotate(int[][] matrix) {
        // m[rows][columns]
        // if len*len%2 != 0 (not even)
        //  then we skip the innermost tile
        int temp = 0, temp2 = 0, len = matrix[0].length, n = len - 1;
        if(len == 1){ return; }
        for(int i = 0; i < len/2 ; i++){
            for(int j = 0; j < (n - (2*i)); j++){
                temp = matrix[0+i][0+i+j]; // temp holds old UL
                matrix[0+i][0+i+j] = matrix[n-i-j][0+i]; // UL = old LL
                temp2 = matrix[0+i+j][n-i]; // temp2 holds old UR
                matrix[0+i+j][n-i] = temp; // UR = old UL = temp
                temp = matrix[n-i][n-i-j]; // temp holds old LR
                matrix[n-i][n-i-j] = temp2; // LR = old UR = temp2
                matrix[n-i-j][0+i] = temp; // LL = old LR = temp
            }
        }
    }
}
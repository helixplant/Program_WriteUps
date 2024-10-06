/*########################
# name: helixplant
# file: sum of two integers
# date: oct. 5, 2024
#
# difficulty: easy
# time to finish: <10mins
# 
# comments:
#   gotta love c yet again
#   this solution beats 100% holy cow
#
#   really simple, just keep shifting right until n is 0
# 
########################*/

int hammingWeight(int n) {
    int i = 0;
    while(n != 0){ //similar to my sum of two ints style
        //large data allowed!
        unsigned long int x = n & 1;
        //shift n right
        n >>= 1;
        //if x (which is always 0bX, where X = 1, 0)
        if(x == 1){
            //inc
            i++;
        }
    }
    return i;
}
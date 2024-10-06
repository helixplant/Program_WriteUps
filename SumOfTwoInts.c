/*########################
# name: helixplant
# file: sum of two integers
# date: oct. 5, 2024
#
# difficulty: medium
# time to finish: <20mins
# 
# comments:
#   gotta love c 
# 
########################*/

int getSum(int a, int b) {
    while(b != 0){ //while b still exists, operations will remove bin from b
        //see if there are any bits to carry, c = carry
        unsigned long int c = a & b; //had to switch since int cant handle some of the numbers
        //add a with b, no carry
        a ^= b;
        //shift carry, so it can be added if necessary on next round
        b = c << 1;
    }
    return a;
}
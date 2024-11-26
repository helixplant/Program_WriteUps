/*########################
# name: helixplant
# file: container with most water
# date: oct. 4, 2024
#
# difficulty: medium
# time to finish: 10mins
# 
# comments:
#   good program
#   pointers have been helpful in solving these sort of problems
# 
########################*/

class ContainerWithMostWater { //had to modify from leetcode, was originally 'Solution'
    public int maxArea(int[] height) {
        //pointers, area, and temp holder
        int i = 0, j = height.length - 1, area = 0, temp = 0;

        if((j+1) == 2){return calcArea(height[0], height[1], 1);} //reduce run time
        //i is on left most side of array and j is on right most side of array
        while(i<j){
            temp = calcArea(height[i], height[j], j-i); //calc new area
            if(temp > area){area = temp;} //mod area if new area (temp) is greater

            if(height[i] < height[j]){
                i++; //move right
            }
            else{
                j--; //move left
            }
        }
        return area;
    }

    //helper
    public int calcArea(int i, int j, int len){
        if(i <= j){ 
            return i*len;}
        return j*len;
    }
}